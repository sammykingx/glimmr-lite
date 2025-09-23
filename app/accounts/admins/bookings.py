from . import admin_bp
from flask import render_template
from faker import Faker

faker = Faker("en_CA")


@admin_bp.route("/view-bookings")
def view_bookings():
    import random
    
    booking_stat = {
        "total_bookings": f"{25784:,}",
        "client_bookings": f"{13856:,}",
        "guest_bookings": f"{8527:,}",
        "returning_bookings": f"{4060:,}",
    }
    
    int_nums = list(range(1,10))
    booking_info = [
        {
            "name": faker.name(),
            "email": faker.safe_email(),
            "phone": faker.phone_number(),
            "status": faker.random_element(elements=("Active", "Inactive", "Guest")),
            "city": faker.city(),
            "province": faker.province_abbr(),
            "bookings": faker.random_int(min=1, max=100),
            "total_spent": f"{round(random.uniform(100, 1_000_000), 2):,.2f}",
            "profile_img": f"user-{int_nums.pop()}.jpeg",
        } for _ in range(9)
    ]
    return render_template(
        "pages/bookings.html",
        role="admin",
        booking_stat=booking_stat,
        booking_info=booking_info
    )