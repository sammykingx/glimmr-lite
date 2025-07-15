import pytz


# Define the timezone for Toronto
TORONRO_TZ = pytz.timezone("America/Toronto")


ALLOWED_SERVICE_CATEGORY = [
    "standard cleaning",
    "deep cleaning",
    "specialized",
]

ALLOWED_SERVICE_TYPE = [
    "regular house cleaning",
    "apartment cleaning",
    "move-in-move/out-cleaning",
    "post-renovation-cleaning",
    "office-cleaning",
    "carpet-cleaning",
    "window-cleaning",
]

ALLOWED_FREQUENCIES = [
    "one-off",
    "weekly",
    "bi-weekly",
    "monthly",
]

ALLOWED_SERVICE_ADDONS = [
    "oven cleaning",
    "fridge cleaning",
    "laundry",
    "ironing",
    "carpet-shampooing",
    "window-washing",
]

ADMIN_EMAILS = [
                "user1@example.com", "user2@example.com", "user3@example.com", 
                "user4@example.com", "user5@example.com", "user6@example.com",
                "user7@example.com", "user8@example.com", "user9@example.com",
                "user10@example.com"
            ]

APP_VERSION = "v1.0.0"
APP_NAME = "Glimmr"
APP_SUPPORT_EMAIL = "support@divgm.com"