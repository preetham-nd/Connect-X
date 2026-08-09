"""Comment table access for admin views."""
from sqlalchemy.orm import joinedload

from models.comment import Comment


class CommentRepository:
    """Read-only comment queries."""

    def count_comments(self) -> int:
        return Comment.query.count()

    def get_all_comments(self):
        return (
            Comment.query.options(joinedload(Comment.user))
            .order_by(Comment.created_at.desc())
            .all()
        )
