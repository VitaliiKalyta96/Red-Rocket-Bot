from app import db


class Event(db.Model):
    __tablename__ = "events"
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