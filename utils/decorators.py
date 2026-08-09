"""Route decorators for access control (Task 8, Task 9)."""
from functools import wraps
from flask import flash, redirect, request, session, url_for

from extensions import db
from models.user import User


def login_required(f):
    """Require a logged-in user. Redirect to login with flash if not."""
    @wraps(f)
    def decorated_view(*args, **kwargs):
        if not session.get("user_id"):
            flash("Please log in to access this page.", "error")
            return redirect(url_for("auth.login", next=request.url))
        return f(*args, **kwargs)
    return decorated_view


def admin_required(f):
    """Restrict route to users with admin role. Block others and redirect with flash."""
    @wraps(f)
    def decorated_view(*args, **kwargs):
        user_id = session.get("user_id")
        if not user_id:
            flash("Please log in to access this page.", "error")
            return redirect(url_for("auth.login", next=request.url))
        user = db.session.get(User, user_id)
        if not user or user.role != "admin":
            flash("You do not have permission to access this page.", "error")
            return redirect(url_for("main.index"))
        return f(*args, **kwargs)
    return decorated_view
