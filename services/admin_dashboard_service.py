"""Admin dashboard use case (Task 14)."""
from typing import Any, Dict, List, Optional

from repositories.comment_repository import CommentRepository
from repositories.post_repository import PostRepository
from repositories.user_repository import UserRepository


class AdminDashboardService:
    """Aggregates repository data for admin monitoring pages."""

    _PREVIEW_LEN = 120
    _COMMENT_PREVIEW_LEN = 160

    def __init__(
        self,
        user_repository: Optional[UserRepository] = None,
        post_repository: Optional[PostRepository] = None,
        comment_repository: Optional[CommentRepository] = None,
    ):
        self._users = user_repository or UserRepository()
        self._posts = post_repository or PostRepository()
        self._comments = comment_repository or CommentRepository()

    def get_dashboard_stats(self) -> Dict[str, int]:
        return {
            "user_count": self._users.count_users(),
            "post_count": self._posts.count_posts(),
            "comment_count": self._comments.count_comments(),
        }

    def get_users_for_admin(self):
        return self._users.get_all_users()

    def get_posts_for_admin(self) -> List[Dict[str, Any]]:
        rows: List[Dict[str, Any]] = []
        for post in self._posts.get_all_posts():
            author = post.user.username if post.user else "—"
            body = post.content or ""
            if len(body) > self._PREVIEW_LEN:
                preview = body[: self._PREVIEW_LEN] + "…"
            else:
                preview = body
            rows.append(
                {
                    "id": post.id,
                    "author_username": author,
                    "content_preview": preview,
                    "created_at": post.created_at,
                }
            )
        return rows

    def get_comments_for_admin(self) -> List[Dict[str, Any]]:
        rows: List[Dict[str, Any]] = []
        for comment in self._comments.get_all_comments():
            author = comment.user.username if comment.user else "—"
            body = comment.content or ""
            if len(body) > self._COMMENT_PREVIEW_LEN:
                preview = body[: self._COMMENT_PREVIEW_LEN] + "…"
            else:
                preview = body
            rows.append(
                {
                    "id": comment.id,
                    "post_id": comment.post_id,
                    "author_username": author,
                    "content_preview": preview,
                    "created_at": comment.created_at,
                }
            )
        return rows
