"""Post table access for admin views."""
from sqlalchemy.orm import joinedload

from models.post import Post


class PostRepository:
    """Read-only post queries."""

    def count_posts(self) -> int:
        return Post.query.count()

    def get_all_posts(self):
        return (
            Post.query.options(joinedload(Post.user))
            .order_by(Post.created_at.desc())
            .all()
        )
