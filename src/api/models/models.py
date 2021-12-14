# from app import db
from app import db


class Event(db.Model):
    __tablename__ = "events"
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name_mentor = db.Column(
        db.String(100),
        nullable=False
    )

    date = db.Column(
        db.String(100),
        nullable=False
    )

    time = db.Column(
        db.String(100),
        nullable=False
    )

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name_mentor': self.name_mentor,
            'date': self.date,
            'time': self.time
        }
