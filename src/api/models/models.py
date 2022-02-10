import uuid

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


class Event(db.Model):
    __tablename__ = "events"
    __table_args__ = {'extend_existing': True}
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(30),
        nullable=False
    )

    description = db.Column(
        db.String(100),
        nullable=False
    )

    date_time = db.Column(
        db.String(30),
        nullable=False
    )

    category = db.Column(
        db.String(100),
        nullable=False
    )

    link = db.Column(
        db.String(100),
        nullable=False
    )

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'date_time': self.date_time,
            'category': self.category,
            'link': self.link,
        }


class Category(db.Model):
    __tablename__ = "category"
    __table_args__ = {'extend_existing': True}
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(30),
        nullable=False
    )

    description = db.Column(
        db.String(100),
        nullable=False
    )

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
        }

class Certificate(db.Model):
    """Data model for user accounts."""
    tablename = 'certificates'
    table_args = {'extend_existing': True}
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    public_id = db.Column(
        db.String,
        default=lambda: str(uuid.uuid4())[:8],
        unique=True)

    title = db.Column(
        db.String(200),
        nullable=False
    )

    description = db.Column(
        db.String(255),
        nullable=False
    )

    owner = db.Column(
        db.String(120),
        nullable=False
    )

    mentor = db.Column(
        db.String(120),
        nullable=False
    )

    date = db.Column(
        db.String(30),
        nullable=False
    )

    @property
    def serialize(self):
        return {
            'public_id': self.public_id,
            'title': self.title,
            'description': self.description,
            'owner': self.owner,
            'mentor': self.mentor,
            'date': self.date,

        }