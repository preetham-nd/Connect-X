"""Like feature routes (Task 12). Naive direct SQL in route handlers."""
from flask import Blueprint, flash, redirect, session, url_for
from sqlalchemy import text

from extensions import db
from utils.decorators import login_required

likes_bp = Blueprint("likes", __name__)


@likes_bp.route("/like/<int:post_id>", methods=["POST"])
@login_required
def like_post(post_id):
    """Like a post once per user. Duplicate likes are blocked."""
    user_id = session.get("user_id")

    post_exists = db.session.execute(
        text("SELECT id FROM posts WHERE id = :post_id"),
        {"post_id": post_id},
    ).first()
    if not post_exists:
        flash("Post not found.", "error")
        return redirect(url_for("main.feed"))

    existing_like = db.session.execute(
        text("SELECT id FROM likes WHERE user_id = :user_id AND post_id = :post_id"),
        {"user_id": user_id, "post_id": post_id},
    ).first()
    if existing_like:
        flash("You already liked this post.", "info")
        return redirect(url_for("main.feed"))

    db.session.execute(
        text("INSERT INTO likes (user_id, post_id) VALUES (:user_id, :post_id)"),
        {"user_id": user_id, "post_id": post_id},
    )
    db.session.commit()
    flash("Post liked.", "success")
    return redirect(url_for("main.feed"))


@likes_bp.route("/unlike/<int:post_id>", methods=["POST"])
@login_required
def unlike_post(post_id):
    """Unlike a post by removing the user-post like row."""
    user_id = session.get("user_id")
    db.session.execute(
        text("DELETE FROM likes WHERE user_id = :user_id AND post_id = :post_id"),
        {"user_id": user_id, "post_id": post_id},
    )
    db.session.commit()
    flash("Like removed.", "success")
    return redirect(url_for("main.feed"))
