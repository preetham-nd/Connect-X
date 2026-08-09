"""Admin routes: Task 14 dashboard (service layer) + Task 15 moderation (naive SQL in routes)."""
from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from sqlalchemy import text

from extensions import db
from models.user import User
from routes.auth import SESSION_ROLE
from services.admin_dashboard_service import AdminDashboardService

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


def _admin_service() -> AdminDashboardService:
    return AdminDashboardService()


def _admin_guard():
    """Task 15: require admin via session role (sync from DB if role missing in session)."""
    uid = session.get("user_id")
    if not uid:
        flash("Please log in to access this page.", "error")
        return redirect(url_for("auth.login", next=request.url))
    if session.get(SESSION_ROLE) != "admin":
        user = db.session.get(User, uid)
        if user and user.role == "admin":
            session[SESSION_ROLE] = "admin"
        else:
            flash("You do not have permission to access this page.", "error")
            return redirect(url_for("main.index"))
    return None


@admin_bp.route("/")
def admin_root():
    err = _admin_guard()
    if err:
        return err
    return redirect(url_for("admin.dashboard"))


@admin_bp.route("/dashboard")
def dashboard():
    err = _admin_guard()
    if err:
        return err
    stats = _admin_service().get_dashboard_stats()
    return render_template(
        "admin/dashboard.html",
        user_count=stats["user_count"],
        post_count=stats["post_count"],
        comment_count=stats["comment_count"],
    )


@admin_bp.route("/users")
def users():
    err = _admin_guard()
    if err:
        return err
    users_list = _admin_service().get_users_for_admin()
    return render_template("admin/users.html", users=users_list)


@admin_bp.route("/posts")
def posts():
    err = _admin_guard()
    if err:
        return err
    posts_list = _admin_service().get_posts_for_admin()
    return render_template("admin/posts.html", posts=posts_list)


@admin_bp.route("/comments")
def comments():
    err = _admin_guard()
    if err:
        return err
    comments_list = _admin_service().get_comments_for_admin()
    return render_template("admin/comments.html", comments=comments_list)


@admin_bp.route("/reports")
def reports():
    err = _admin_guard()
    if err:
        return err
    rows = db.session.execute(
        text("SELECT id, content_type, content_id, reason, created_at FROM reported_content ORDER BY id DESC")
    ).mappings().all()
    return render_template("admin/reports.html", reports=rows)


@admin_bp.route("/delete/post/<int:post_id>", methods=["POST"])
def delete_post(post_id):
    err = _admin_guard()
    if err:
        return err
    db.session.execute(text("DELETE FROM posts WHERE id = :pid"), {"pid": post_id})
    db.session.commit()
    flash("Post deleted.", "success")
    return redirect(url_for("admin.dashboard"))


@admin_bp.route("/delete/comment/<int:comment_id>", methods=["POST"])
def delete_comment(comment_id):
    err = _admin_guard()
    if err:
        return err
    db.session.execute(text("DELETE FROM comments WHERE id = :cid"), {"cid": comment_id})
    db.session.commit()
    flash("Comment deleted.", "success")
    return redirect(url_for("admin.comments"))


@admin_bp.route("/block/user/<int:user_id>", methods=["POST"])
def block_user(user_id):
    err = _admin_guard()
    if err:
        return err
    admin_uid = session.get("user_id")
    if user_id == admin_uid:
        flash("You cannot block yourself.", "error")
        return redirect(url_for("admin.users"))
    row = db.session.execute(
        text("SELECT role FROM user WHERE id = :uid"),
        {"uid": user_id},
    ).first()
    if not row:
        flash("User not found.", "error")
        return redirect(url_for("admin.users"))
    if row[0] == "admin":
        flash("Cannot block an admin account.", "error")
        return redirect(url_for("admin.users"))
    db.session.execute(
        text("UPDATE user SET is_blocked = 1 WHERE id = :uid"),
        {"uid": user_id},
    )
    db.session.commit()
    flash("User blocked.", "success")
    return redirect(url_for("admin.users"))


@admin_bp.route("/unblock/user/<int:user_id>", methods=["POST"])
def unblock_user(user_id):
    err = _admin_guard()
    if err:
        return err
    db.session.execute(
        text("UPDATE user SET is_blocked = 0 WHERE id = :uid"),
        {"uid": user_id},
    )
    db.session.commit()
    flash("User unblocked.", "success")
    return redirect(url_for("admin.users"))
