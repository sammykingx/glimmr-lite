# holds all payment related services

class PaymentService:
    def __init__(self, booking):
        self.booking = booking

    def process_payment(self, payment_gateway):
        """Processes the payment for the booking."""
        
        if not self.booking:
            raise ValueError("Booking is not set.")
        
        # Assuming payment_gateway has a charge method
        result = payment_gateway.charge(self.booking.price, self.booking.user)
        
        if not result["success"]:
            raise Exception("Payment failed: " + result["message"])
        
    
        return True