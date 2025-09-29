from app.extensions import db

class UserAddress(db.Model):
    __tablename__ = "user_addresses"

    id = db.Column(db.Integer, primary_key=True)

    # Relationship to user
    user_id = db.Column(db.Integer, db.ForeignKey("user_profiles.id"), nullable=False)
    user = db.relationship("UserProfile", backref="addresses")

    # Address fields
    street_line_1 = db.Column(db.String(150), nullable=False)
    street_line_2 = db.Column(db.String(150), nullable=True)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=True)
    zipcode = db.Column(db.String(20), nullable=True)
    country = db.Column(db.String(100), nullable=False)

    # Geolocation fields
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)

    # Optional / metadata
    label = db.Column(db.String(50), nullable=True)  # e.g., "Home", "Office"
    is_primary = db.Column(db.Boolean, default=False)  # mark main address
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def __repr__(self):
        return f"<UserAddress {self.street_line_1}, {self.city}, {self.country}>"

    def to_dict(self):
        """
        Useful for API responses or your services.
        """
        return {
            "id": self.id,
            "street_line_1": self.street_line_1,
            "street_line_2": self.street_line_2,
            "city": self.city,
            "state": self.state,
            "zipcode": self.zipcode,
            "country": self.country,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "label": self.label,
            "is_primary": self.is_primary,
        }
