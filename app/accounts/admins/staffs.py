from . import admin_bp
from flask import render_template
from faker import Faker


faker = Faker("en_CA")


@admin_bp.route("/all-staffs")
def view_staffs():
    import random

    staffs_stat = {
        "total_staffs": f"{57:,}",
        "active_staffs": f"{50:,}",
        "cleaning_agent": f"{7:,}",
        "managers": f"{5:,}",
    }

    int_nums = list(range(1, 10))
    staffs_info = [
        {
            "name": faker.name(),
            "email": faker.safe_email(),
            "phone": faker.phone_number(),
            "status": faker.random_element(elements=("manager", "agent", "admin")),
            "city": faker.city(),
            "province": faker.province_abbr(),
            "role": faker.random_element(elements=("Admin", "Agent", "Manager")),
            "profile_img": f"user-{int_nums.pop()}.jpeg",
        } for _ in range(9)
    ]
    
    return render_template(
        "pages/staffs.html",
        role="admin",
        staff_stats=staffs_stat,
        staffs_info=staffs_info,
    )