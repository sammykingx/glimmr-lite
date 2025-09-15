from . import admin_bp
from flask import render_template
from faker import Faker

faker = Faker("en_CA")

@admin_bp.route("/all-clients")
def view_clients():
    import random
    
    clients_stat = {
        "total_clients": f"{1174:,}",
        "registered_clients": f"{1000:,}",
        "guest_clients": f"{174:,}",
        "active_clients": f"{700:,}",
    }
    
    int_nums = list(range(1,10))
    clients_info = [
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
        "pages/clients.html",
        role="admin",
        clients_stat=clients_stat,
        clients_info=clients_info,
    )