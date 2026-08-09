"""Authentication routes: registration (Task 5), login & session (Task 7)."""
import re
from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from sqlalchemy import text

from extensions import db
from models.user import User
from utils.password import hash_password, verify_password

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

# Session keys for logged-in user
SESSION_USER_ID = "user_id"
SESSION_USERNAME = "username"
SESSION_ROLE = "role"

# Simple email format check
EMAIL_RE = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")


def _validate_registration(username: str, email: str, password: str, confirm_password: str) -> list[str]:
    """Validate registration input. Returns list of error messages (empty if valid)."""
    errors = []
    username = (username or "").strip()
    email = (email or "").strip().lower()
    password = password or ""
    confirm_password = confirm_password or ""

    if not username:
        errors.append("Username is required.")
    if not email:
        errors.append("Email is required.")
    elif not EMAIL_RE.match(email):
        errors.append("Please enter a valid email address.")
    if not password:
        errors.append("Password is required.")
    if password and confirm_password != password:
        errors.append("Password and confirm password do not match.")

    if not errors and email:
        existing = User.query.filter_by(email=email).first()
        if existing:
            errors.append("An account with this email already exists.")
    if not errors and username:
        existing = User.query.filter_by(username=username).first()
        if existing:
            errors.append("This username is already taken.")

    return errors


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    """Display login form (GET) or process login (POST)."""
    if request.method == "GET":
        return render_template("login.html")

    email = request.form.get("email", "").strip().lower()
    password = request.form.get("password", "")

    if not email or not password:
        flash("Email and password are required.", "error")
        return render_template("login.html", email=email)

    user = User.query.filter_by(email=email).first()
    if not user or not verify_password(user.password_hash, password):
        flash("Invalid email or password.", "error")
        return render_template("login.html", email=email)

    blocked = db.session.execute(
        text("SELECT is_blocked FROM user WHERE id = :id"),
        {"id": user.id},
    ).scalar()
    if blocked:
        flash("Your account has been blocked.", "error")
        return render_template("login.html", email=email)

    session[SESSION_USER_ID] = user.id
    session[SESSION_USERNAME] = user.username
    session[SESSION_ROLE] = user.role
    flash("You are now logged in.", "success")
    if user.role == "admin":
        return redirect(url_for("admin.dashboard"))
    return redirect(url_for("main.index"))


@auth_bp.route("/logout", methods=["GET", "POST"])
def logout():
    """Clear session and redirect to home."""
    session.clear()
    flash("You have been logged out.", "success")
    return redirect(url_for("main.index"))


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    """Display registration form (GET) or process submission (POST)."""
    if request.method == "GET":
        return render_template("register.html")

    username = request.form.get("username", "").strip()
    email = request.form.get("email", "").strip().lower()
    password = request.form.get("password", "")
    confirm_password = request.form.get("confirm_password", "")

    errors = _validate_registration(username, email, password, confirm_password)
    if errors:
        for msg in errors:
            flash(msg, "error")
        return render_template(
            "register.html",
            username=username,
            email=email,
        )

    user = User(
        username=username,
        email=email,
        password_hash=hash_password(password),
        role="user",
    )
    db.session.add(user)
    db.session.commit()
    flash("Account created successfully. You can log in when login is available.", "success")
    return redirect(url_for("main.index"))
