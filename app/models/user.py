from app import db
from datetime import datetime, timezone
from sqlalchemy.sql import func


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(250), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    role_id = db.Column(db.Integer, nullable=False)
    booking = db.relationship('Booking', backref='user', lazy=True)

    def __repr__(self):
        return f'User <{self.first_name} {self.last_name}>'
