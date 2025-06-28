# sends notifications to the user and admin


class NotificationService:
    @staticmethod
    def send_to_customer(booking):
        """Send booking confirmation to the customer."""
        # Here you would implement the logic to send an email or notification
        # print(f"Sending booking confirmation to {booking.user.email} for booking ID {booking.id}")
        print("sending mail to customer")

    @staticmethod
    def send_to_admin(booking):
        """Send booking details to the admin."""
        # Here you would implement the logic to send an email or notification to the admin
        #print(f"Sending booking details to admin for booking ID {booking.id}")
        print("sending mail to admin")