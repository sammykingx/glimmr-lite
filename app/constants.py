import pytz


# Define the timezone for Toronto
TORONRO_TZ = pytz.timezone("America/Toronto")


ALLOWED_SERVICE = {
    "residential cleaning": [
        "house cleaning", "deep cleaning",
        "move-in-out cleaning", "airbnb cleaning",
    ],
    "commercial cleaning": {
        "small": {"size": "<2,000sqft", "multiplier": 0.2},
        "medium": {"size": "2,000sqft - 5,000sqft", "multiplier": 0.18},
        "large": {"size": "5,000sqft - 10,000sqft", "multiplier": 0.16},
        "custom": {"size": ">10,000sqft"},
    },
    "church cleaning": {
        "small": {"size": "<3,000sqft", "amount": 180},
        "medium": {"size": "3,000sqft - 6,000sqft", "amount": 300},
        "large": {"size": ">6,000sqft", "amount": 500},
    },
    "child care": {
        "small": {"size": "<2,000sqft", "amount": 250},
        "medium": {"size": "<2,000sqft - 5,000sqft", "amount": 350},
        "large": {"size": ">5,000sqft", "amount": 500},
    },
    "gym": {
        "small": {"size": "<3,000sqft", "amount": 300},
        "medium": {"size": "<3,000sqft - 7,000sqft", "amount": 450},
        "large": {"size": ">7,000sqft", "amount": 650},
    },
    "salon cleaning": {
        "small": {"size": "<1,500sqft", "amount": 150},
        "medium": {"size": "1,500sqft - 3,000sqft", "amount": 200},
        "large": {"size": ">3,000sqft", "amount": 300},
    },
    "retail cleaning": {
        "small": {"size": "<3,000sqft", "amount": 200},
        "medium": {"size": "2,000sqft - 5,000sqft", "amount": 350},
        "large": {"size": ">5,000sqft", "amount": 500},
    },
    "office cleaning": {
        "small": {"size": "<2,000sqft", "amount": 180},
        "medium": {"size": "2,000sqft - 5,000sqft", "amount": 300},
        "large": {"size": ">5,000sqft", "amount": 500},
    }
}

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
    {"name" : "interior window cleaning", "amount": 50, "max": 10},
    {"name": "blinds dusting", "amount":20, "max": 10},
    {"name": "oven cleaning", "amount": 30},
    {"name": "fridge cleaning", "amount":25},
    {"name": "laundry", "amount": 35, "max": "2 loads"},
    {"name": "Basement cleaning", "amount":70},
    {"name": "garage cleaning", "amount":60},
    {"name": "porch/balcony cleaning", "amount":25},
    {"name": "driveway sweeping", "amount":30},
]

ADMIN_EMAILS = [
                "user1@example.com", "user2@example.com", "user3@example.com", 
                "user4@example.com", "user5@example.com", "user6@example.com",
                "user7@example.com", "user8@example.com", "user9@example.com",
                "user10@example.com"
            ]

APP_VERSION = "v1.0.0"
APP_NAME = "Glimmr"
APP_SUPPORT_EMAIL = "support@oliveglitters.com"