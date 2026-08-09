"""User table access for admin views."""
from models.user import User


class UserRepository:
    """Read-only user queries."""

    def count_users(self) -> int:
        return User.query.count()

    def get_all_users(self):
        return User.query.order_by(User.id.asc()).all()
