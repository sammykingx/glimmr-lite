from faker import Faker
from app.constants import ALLOWED_SERVICE, ALLOWED_FREQUENCIES, ALLOWED_SERVICE_ADDONS


faker = Faker("en_CA")


# Sample data for testing
# This data is used to test the booking endpoint.
def create_sample_data():
    """Creates sample data for testing the booking endpoint."""
    from datetime import datetime

    return {
        "category": faker.random_element(elements=ALLOWED_SERVICE.keys()),
        "service": faker.random_element(elements=ALLOWED_SERVICE.values()),
        "bedrooms": faker.random_int(min=1, max=6),
        "bathrooms": faker.random_int(min=1, max=3),
        "frequency": faker.random_element(elements=ALLOWED_FREQUENCIES),
        "addOns": [
            faker.random_element(elements=ALLOWED_SERVICE_ADDONS)
            for _ in range(faker.random_int(min=0, max=3))
        ],
        "selectedDate": datetime.now().date(),
        "selectedTime": str(datetime.now().time()),
        "personalInfo": {
            "firstName": faker.first_name(),
            "lastName": faker.last_name(),
            "email": faker.email(),
            "phone": faker.phone_number(),
        },
        "address": {
            "street": faker.street_address(),
            "city": faker.city(),
            "state": faker.administrative_unit(),
            "zipCode": faker.postalcode(),
        },
        "price": float(
            faker.random_element(
                elements=[
                    faker.pydecimal(left_digits=2, right_digits=2, positive=True)
                    for _ in range(10)
                ]
            )
        ),
        "additionalInfo": faker.sentence(),
    }


def bad_demo_data():
    return {
        "category": "Standard Cleaning",  # Invalid category
        "service": "Regular House Cleaning",  # Invalid service
        "bedrooms": 1,
        "bathrooms": 1,
        "frequency": "weekly",
        "addOns": [],
        "selectedDate": "2025-06-30",
        "selectedTime": "10:00",
        "personalInfo": {
            "firstName": "Moon",
            "lastName": "Chaser",
            "email": "nelly@mailer.com",
            "phone": "08056109384",
        },
        "address": {
            "street": faker.street_address(),
            "city": faker.city(),
            "state": faker.state(),
            "zipCode": faker.zipcode(),
        },
        "additionalInfo": "no additional info",
    }
