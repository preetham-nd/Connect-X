"""Test model for verifying database connectivity (Task 4)."""
from datetime import datetime
from extensions import db


class ConnectionTest(db.Model):
    """Maps to connection_test table."""

    __tablename__ = "connection_test"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
