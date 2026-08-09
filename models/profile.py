"""Profile model (Task 9). Additional user info; one-to-one with User."""
from datetime import datetime
from extensions import db


class Profile(db.Model):
    """Maps to profile table. Linked to user via user_id."""

    __tablename__ = "profile"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False, unique=True)
    display_name = db.Column(db.String(120), nullable=True)
    bio = db.Column(db.String(500), nullable=True)
    profile_image = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = db.relationship("User", backref=db.backref("profile", uselist=False))

    def __repr__(self):
        return f"<Profile user_id={self.user_id}>"
