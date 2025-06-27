from app.extensions import db
from datetime import date, datetime
from app.constants import TORONRO_TZ


class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True, index=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    address= db.relationship('Address', backref='user', lazy=True)
    bookings = db.relationship('Booking', backref='user', lazy=True)
    
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
    
    id = db.Column(db.Integer, primary_key=True, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    service = db.Column(db.String(50), nullable=False)
    service_category = db.Column(db.String(50), nullable=False)
    bedrooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Integer, nullable=False)
    frequency = db.Column(db.String(20), default="one-off",)
    add_ons = db.Column(db.JSON)
    booking_date = db.Column(db.Date, default=date.today())
    booking_time = db.Column(db.Time, default=datetime.now(TORONRO_TZ).time(), nullable=False)
    price = db.Column(db.Float, nullable=False, default=0.0)
    recurring = db.Column(db.Boolean, default=False)
    status = db.Column(db.String(20), default="pending")
    payment_status = db.Column(db.String(20), default="unpaid")
    additional_info = db.Column(db.Text)
    
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
        
class Address(db.Model):
    __tablename__ = 'addresses'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    street = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    zip_code = db.Column(db.String(20), nullable=False)
    
    def to_dict(self):
        return {
            'street': self.street,
            'city': self.city,
            'state': self.state,
            'zip_code': self.zip_code
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            street=data.get('street'),
            city=data.get('city'),
            state=data.get('state'),
            zip_code=data.get('zip_code')
        )
class RecurringBooking(db.Model):
    __tablename__ = 'recurring_bookings'
    
    id = db.Column(db.Integer, primary_key=True)
    booking_id = db.Column(db.Integer, db.ForeignKey('bookings.id'), nullable=False)
    frequency = db.Column(db.String(20), nullable=False)
    
    booking = db.relationship('Booking', backref=db.backref('recurring_bookings', lazy=True))
    
    def __repr__(self):
        return f'<RecurringBooking {self.id}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'booking_id': self.booking_id,
            'frequency': self.frequency
        }