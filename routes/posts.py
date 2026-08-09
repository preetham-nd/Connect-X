"""Post routes (Task 10): create, edit, delete. Feed is in main.feed. Owner-only for edit/delete."""
from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from sqlalchemy import text

from extensions import db
from models.post import Post
from utils.decorators import login_required

posts_bp = Blueprint("posts", __name__, url_prefix="/posts")

MAX_CONTENT_LENGTH = 1000


def _get_post_or_404(post_id: int) -> Post:
    return Post.query.get_or_404(post_id)


def _is_post_owner(post: Post) -> bool:
    return session.get("user_id") == post.user_id


@posts_bp.route("/")
@login_required
def index():
    """Redirect /posts to feed."""
    return redirect(url_for("main.feed"))


@posts_bp.route("/create", methods=["GET", "POST"])
@login_required
def create():
    """Show create form (GET) or create a new post (POST)."""
    uid = session["user_id"]
    blocked = db.session.execute(
        text("SELECT is_blocked FROM user WHERE id = :id"),
        {"id": uid},
    ).scalar()
    if blocked:
        flash("Your account has been blocked.", "error")
        return redirect(url_for("main.feed"))

    if request.method == "GET":
        return render_template("posts/create.html")
    content = (request.form.get("content") or "").strip()
    if not content:
        flash("Post content is required.", "error")
        return render_template("posts/create.html", content=content)
    if len(content) > MAX_CONTENT_LENGTH:
        flash(f"Content must be at most {MAX_CONTENT_LENGTH} characters.", "error")
        return render_template("posts/create.html", content=content)
    post = Post(user_id=session["user_id"], content=content)
    db.session.add(post)
    db.session.commit()
    flash("Post created.", "success")
    return redirect(url_for("main.feed"))


@posts_bp.route("/<int:post_id>/edit", methods=["GET", "POST"])
@login_required
def edit(post_id: int):
    """Edit post (owner only)."""
    post = _get_post_or_404(post_id)
    if not _is_post_owner(post):
        flash("You can only edit your own posts.", "error")
        return redirect(url_for("main.feed"))
    if request.method == "GET":
        return render_template("posts/edit.html", post=post)
    content = (request.form.get("content") or "").strip()
    if not content:
        flash("Post content is required.", "error")
        return render_template("posts/edit.html", post=post, content=content)
    if len(content) > MAX_CONTENT_LENGTH:
        flash(f"Content must be at most {MAX_CONTENT_LENGTH} characters.", "error")
        return render_template("posts/edit.html", post=post, content=content)
    post.content = content
    db.session.commit()
    flash("Post updated.", "success")
    return redirect(url_for("main.feed"))


@posts_bp.route("/<int:post_id>/delete", methods=["POST"])
@login_required
def delete(post_id: int):
    """Delete post (owner only). Permanently removed."""
    post = _get_post_or_404(post_id)
    if not _is_post_owner(post):
        flash("You can only delete your own posts.", "error")
        return redirect(url_for("main.feed"))
    db.session.delete(post)
    db.session.commit()
    flash("Post deleted.", "success")
    return redirect(url_for("main.feed"))
