"""Main routes - home, feed, users listing, db test."""
from flask import Blueprint, flash, jsonify, redirect, render_template, request, session, url_for
from sqlalchemy import text

from extensions import db
from models.connection_test import ConnectionTest
from models.post import Post
from models.user import User
from utils.decorators import login_required

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    """Home page - confirms the Flask server is running."""
    return render_template("index.html")


@main_bp.route("/feed")
@login_required
def feed():
    """Main feed page: all posts, newest first. Author link to profile. Edit/delete only for author."""
    posts = Post.query.order_by(Post.created_at.desc()).all()
    like_counts = {}
    comments_by_post = {}
    for post in posts:
        count = db.session.execute(
            text("SELECT COUNT(*) FROM likes WHERE post_id = :post_id"),
            {"post_id": post.id},
        ).scalar()
        like_counts[post.id] = count or 0
        comments = db.session.execute(
            text(
                "SELECT c.id, c.user_id, c.content, c.created_at, u.username "
                "FROM comments c "
                "JOIN user u ON u.id = c.user_id "
                "WHERE c.post_id = :post_id "
                "ORDER BY c.created_at DESC"
            ),
            {"post_id": post.id},
        ).mappings().all()
        comments_by_post[post.id] = comments

    liked_post_ids = set()
    user_id = session.get("user_id")
    if user_id:
        for post in posts:
            liked = db.session.execute(
                text(
                    "SELECT id FROM likes WHERE user_id = :user_id AND post_id = :post_id"
                ),
                {"user_id": user_id, "post_id": post.id},
            ).first()
            if liked:
                liked_post_ids.add(post.id)

    return render_template(
        "feed.html",
        posts=posts,
        like_counts=like_counts,
        liked_post_ids=liked_post_ids,
        comments_by_post=comments_by_post,
    )


@main_bp.route("/report/post/<int:post_id>", methods=["POST"])
@login_required
def report_post(post_id):
    """Submit a post report into reported_content for admins."""
    uid = session["user_id"]
    blocked = db.session.execute(
        text("SELECT is_blocked FROM user WHERE id = :id"),
        {"id": uid},
    ).scalar()
    if blocked:
        flash("Your account has been blocked.", "error")
        return redirect(url_for("main.feed"))

    row = db.session.execute(
        text("SELECT id, user_id FROM posts WHERE id = :pid"),
        {"pid": post_id},
    ).first()
    if not row:
        flash("Post not found.", "error")
        return redirect(url_for("main.feed"))
    if row[1] == uid:
        flash("You cannot report your own post.", "error")
        return redirect(url_for("main.feed"))

    reason = (request.form.get("reason") or "").strip() or None
    db.session.execute(
        text(
            "INSERT INTO reported_content (content_type, content_id, reason) "
            "VALUES ('post', :pid, :reason)"
        ),
        {"pid": post_id, "reason": reason},
    )
    db.session.commit()
    flash("Thanks — your report was submitted for review.", "success")
    return redirect(url_for("main.feed"))


@main_bp.route("/users")
@login_required
def users_list():
    """List all users with links to their profiles."""
    users = User.query.order_by(User.username).all()
    return render_template("users_list.html", users=users)


@main_bp.route("/db-test")
def db_test():
    """Verify database connectivity: insert a record, retrieve it, return result."""
    record = ConnectionTest(name="db_test_record")
    db.session.add(record)
    db.session.commit()
    fetched = ConnectionTest.query.filter_by(id=record.id).first()
    return jsonify(fetched.to_dict())
