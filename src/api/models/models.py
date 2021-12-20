from src.api.app import db
from datetime import datetime


class User(db.Model):
    """Data model for user accounts."""
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    username = db.Column(
        db.String(64),
        index=False,
        unique=True,
        nullable=False
    )
    password = db.Column(
        db.String(200),
        unique=False,
        nullable=False
    )
    email = db.Column(
        db.String(80),
        index=True,
        unique=True,
        nullable=False
    )
    created = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        index=False,
        unique=False,
        nullable=False,

    )

    admin = db.Column(
        db.Boolean,
        index=False,
        unique=False,
        default=False
    )

    def __repr__(self):
        return '<User {}>'.format(self.username)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email

        }
