"""Profile routes (Task 9): view own, view other, edit (owner only)."""
import os
import uuid
from flask import Blueprint, current_app, flash, redirect, render_template, request, session, url_for

from extensions import db
from models.profile import Profile
from models.user import User
from utils.decorators import login_required

profile_bp = Blueprint("profile", __name__, url_prefix="/profile")


def _get_or_create_profile(user_id: int) -> Profile:
    """Get existing profile or create one for the user."""
    profile = Profile.query.filter_by(user_id=user_id).first()
    if not profile:
        profile = Profile(user_id=user_id)
        db.session.add(profile)
        db.session.commit()
    return profile


def _allowed_image(filename: str) -> bool:
    ext = filename.rsplit(".", 1)[-1].lower() if "." in filename else ""
    return ext in current_app.config.get("ALLOWED_IMAGE_EXTENSIONS", {"png", "jpg", "jpeg", "gif", "webp"})


def _save_profile_image(file, user_id: int):
    """Save uploaded file to static/uploads/profiles. Return path relative to static/ or None."""
    if not file or file.filename == "" or not _allowed_image(file.filename):
        return None
    upload_folder = current_app.config["UPLOAD_FOLDER"]
    root = current_app.root_path
    full_dir = os.path.join(root, upload_folder)
    os.makedirs(full_dir, exist_ok=True)
    ext = file.filename.rsplit(".", 1)[-1].lower()
    name = f"{user_id}_{uuid.uuid4().hex[:12]}.{ext}"
    full_path = os.path.join(full_dir, name)
    file.save(full_path)
    return f"uploads/profiles/{name}"


@profile_bp.route("/")
@login_required
def view_own():
    """Redirect to the current user's profile page."""
    return redirect(url_for("profile.view", user_id=session["user_id"]))


@profile_bp.route("/<int:user_id>")
@login_required
def view(user_id: int):
    """View a user's profile (own or another user). Edit link only for owner."""
    user = User.query.get_or_404(user_id)
    profile = Profile.query.filter_by(user_id=user_id).first()
    if not profile:
        profile = _get_or_create_profile(user_id)
    current_user_id = session.get("user_id")
    is_owner = current_user_id == user_id
    return render_template(
        "profile/view.html",
        user=user,
        profile=profile,
        is_owner=is_owner,
    )


@profile_bp.route("/<int:user_id>/edit", methods=["GET", "POST"])
@login_required
def edit(user_id: int):
    """Edit profile (owner only). No email/password fields."""
    if session["user_id"] != user_id:
        flash("You can only edit your own profile.", "error")
        return redirect(url_for("main.index"))
    user = User.query.get_or_404(user_id)
    profile = _get_or_create_profile(user_id)
    if request.method == "GET":
        return render_template("profile/edit.html", user=user, profile=profile)
    display_name = request.form.get("display_name", "").strip() or None
    bio = request.form.get("bio", "").strip() or None
    profile.display_name = display_name
    profile.bio = bio
    file = request.files.get("profile_image")
    if file and file.filename:
        if not _allowed_image(file.filename):
            flash("Invalid image type. Use PNG, JPG, JPEG, GIF, or WebP.", "error")
            return render_template("profile/edit.html", user=user, profile=profile)
        new_path = _save_profile_image(file, user_id)
        if new_path:
            profile.profile_image = new_path
    db.session.commit()
    flash("Profile updated.", "success")
    return redirect(url_for("profile.view", user_id=user_id))
