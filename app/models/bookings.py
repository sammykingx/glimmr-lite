from app.extensions import db
from datetime import datetime
from enum import Enum
from app.constants.app_meta import TORONTO_TZ


class FrequencyEnum(Enum):
    ONE_OFF = "one_off"
    WEEKLY = "weekly"
    BIWEEKLY = "biweekly"
    MONTHLY = "monthly"

class Booking(db.Model):
    __tablename__ = "bookings"

    id = db.Column(db.Integer, primary_key=True, index=True)
    booking_id = db.Column(db.String(15), unique=True, nullable=False, index=True)
    user_email = db.Column(
        db.Integer, db.ForeignKey("user_profiles.email"), nullable=False, index=True
    )
    service = db.Column(db.String(50), nullable=False)
    service_category = db.Column(db.String(50), nullable=False)
    bedrooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.String(12), nullable=False)
    frequency = db.Column(db.Enum(FrequencyEnum), default=FrequencyEnum.ONE_OFF, nullable=False)
    add_ons = db.Column(db.JSON)
    cleaning_date = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(TORONTO_TZ))
    updated_at = db.Column(db.DateTime, default=datetime.now(TORONTO_TZ), onupdate=datetime.now(TORONTO_TZ))
    price = db.Column(db.Float, nullable=False, default=0.0)
    recurring = db.Column(db.Boolean, default=False)
    status = db.Column(db.String(20), default="pending")
    payment_status = db.Column(db.String(20), default="unpaid")
    paid_at = db.Column(
        db.DateTime,
    )
    additional_info = db.Column(db.Text)
