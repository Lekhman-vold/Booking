from app import db
from datetime import datetime


class Facility(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)

    rental_id = db.Column(db.Integer, db.ForeignKey('rental.id'),
        nullable=False)
    rental = db.relationship('Rental',
        backref=db.backref('facility', lazy=True))

    def __repr__(self):
        return '<Facility %r>' % self.name


class Rental(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    from_at = db.Column(db.Date, nullable=False)
    to_at = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'Rental from: {self.from_at} to {self.to_at}'
