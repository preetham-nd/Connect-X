"""Post model (Task 10). User-generated content linked to author."""
from datetime import datetime
from extensions import db


class Post(db.Model):
    """Maps to posts table. Each post belongs to one user."""

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    content = db.Column(db.String(1000), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = db.relationship("User", backref=db.backref("posts", lazy="dynamic"))

    def __repr__(self):
        return f"<Post {self.id} by user {self.user_id}>"
