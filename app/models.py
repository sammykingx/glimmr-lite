from flask_sqlalchemy import SQLAlchemy
from app.extensions import db


class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    
    def __repr__(self):
        return f'<User {self.username}>'
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone': self.phone
        }
        
    @classmethod
    def from_dict(cls, data):
        return cls(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            email=data.get('email'),
            phone=data.get('phone')
        )
        
class Booking(db.Model):
    __tablename__ = 'bookings'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    booking_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    
    user = db.relationship('User', backref=db.backref('bookings', lazy=True))
    
    def __repr__(self):
        return f'<Booking {self.id}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'booking_date': self.booking_date.isoformat(),
            'status': self.status
        }
        
    @classmethod
    def from_dict(cls, data):
        return cls(
            user_id=data.get('user_id'),
            booking_date=data.get('booking_date'),
            status=data.get('status')
        )