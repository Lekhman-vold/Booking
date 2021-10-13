from app import db
from datetime import datetime
from sqlalchemy.sql import func


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(50), nullable=False)
    room_type = db.Column(db.String(15), nullable=False)
    is_booked = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.DateTime, default=func.now())

    def __repr__(self):
        return f'Room: {self.number} Type: {self.room_type} Booked: {self.is_booked}'


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.Integer, db.ForeignKey('user.id'))
    room_number = db.Column(db.Integer, db.ForeignKey('room.id'))
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'Room<{self.room_number}> Booking from: {self.start_date} to {self.end_date}'

