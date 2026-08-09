"""Comment routes (Task 13). Naive direct SQL approach."""
from flask import Blueprint, flash, redirect, request, session, url_for
from sqlalchemy import text

from extensions import db
from utils.decorators import login_required

comments_bp = Blueprint("comments", __name__, url_prefix="/comments")


@comments_bp.route("/add/<int:post_id>", methods=["POST"])
@login_required
def add_comment(post_id):
    """Add a comment to a post. Empty comments are not allowed."""
    user_id = session.get("user_id")
    blocked = db.session.execute(
        text("SELECT is_blocked FROM user WHERE id = :id"),
        {"id": user_id},
    ).scalar()
    if blocked:
        flash("Your account has been blocked.", "error")
        return redirect(url_for("main.feed"))

    content = (request.form.get("content") or "").strip()
    if not content:
        flash("Comment cannot be empty.", "error")
        return redirect(url_for("main.feed"))

    post_exists = db.session.execute(
        text("SELECT id FROM posts WHERE id = :post_id"),
        {"post_id": post_id},
    ).first()
    if not post_exists:
        flash("Post not found.", "error")
        return redirect(url_for("main.feed"))

    db.session.execute(
        text(
            "INSERT INTO comments (user_id, post_id, content) "
            "VALUES (:user_id, :post_id, :content)"
        ),
        {"user_id": user_id, "post_id": post_id, "content": content},
    )
    db.session.commit()
    flash("Comment added.", "success")
    return redirect(url_for("main.feed"))


@comments_bp.route("/delete/<int:comment_id>", methods=["POST"])
@login_required
def delete_comment(comment_id):
    """Delete comment only if it belongs to logged-in user."""
    user_id = session.get("user_id")
    row = db.session.execute(
        text("SELECT id, user_id FROM comments WHERE id = :comment_id"),
        {"comment_id": comment_id},
    ).first()
    if not row:
        flash("Comment not found.", "error")
        return redirect(url_for("main.feed"))

    if row[1] != user_id:
        flash("You can only delete your own comments.", "error")
        return redirect(url_for("main.feed"))

    db.session.execute(
        text("DELETE FROM comments WHERE id = :comment_id"),
        {"comment_id": comment_id},
    )
    db.session.commit()
    flash("Comment deleted.", "success")
    return redirect(url_for("main.feed"))
