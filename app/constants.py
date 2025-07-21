import pytz


# Define the timezone for Toronto
TORONRO_TZ = pytz.timezone("America/Toronto")


ALLOWED_SERVICE = {
    "residential_cleaning": {
        "type": "list",
        "options": [
            "house_cleaning",
            "deep_cleaning",
            "move_in_move_out_cleaning",
            "airbnb_cleaning"
        ]
    },
    "commercial_cleaning": {
        "type": "size_based",
        "sizes": {
            "small": {"label": "<2,000sqft", "multiplier": 0.2},
            "medium": {"label": "2,000sqft - 5,000sqft", "multiplier": 0.18},
            "large": {"label": "5,000sqft - 10,000sqft", "multiplier": 0.16},
            "custom": {"label": ">10,000sqft"}
        }
    },
    "church_cleaning": {
        "type": "size_based",
        "sizes": {
            "small": {"label": "<3,000sqft", "amount": 180},
            "medium": {"label": "3,000sqft - 6,000sqft", "amount": 300},
            "large": {"label": ">6,000sqft", "amount": 500}
        }
    },
    "child_care": {
        "type": "size_based",
        "sizes": {
            "small": {"label": "<2,000sqft", "amount": 250},
            "medium": {"label": "2,000sqft - 5,000sqft", "amount": 350},
            "large": {"label": ">5,000sqft", "amount": 500}
        }
    },
    "gym": {
        "type": "size_based",
        "sizes": {
            "small": {"label": "<3,000sqft", "amount": 300},
            "medium": {"label": "3,000sqft - 7,000sqft", "amount": 450},
            "large": {"label": ">7,000sqft", "amount": 650}
        }
    },
    "salon_cleaning": {
        "type": "size_based",
        "sizes": {
            "small": {"label": "<1,500sqft", "amount": 150},
            "medium": {"label": "1,500sqft - 3,000sqft", "amount": 200},
            "large": {"label": ">3,000sqft", "amount": 300}
        }
    },
    "retail_cleaning": {
        "type": "size_based",
        "sizes": {
            "small": {"label": "<3,000sqft", "amount": 200},
            "medium": {"label": "2,000sqft - 5,000sqft", "amount": 350},
            "large": {"label": ">5,000sqft", "amount": 500}
        }
    },
    "office_cleaning": {
        "type": "size_based",
        "sizes": {
            "small": {"label": "<2,000sqft", "amount": 180},
            "medium": {"label": "2,000sqft - 5,000sqft", "amount": 300},
            "large": {"label": ">5,000sqft", "amount": 500}
        }
    }
}

RESIDENTIAL_SERVICE_PRICING = {
    "house_cleaning": {
    1: { "studio": 90, 1: 110, 2: 120 },
    2: { 1: 130, 2: 145, 3: 160 },
    3: { 1: 145, 2: 160, 3: 175 },
    4: { 1: 175, 2: 190, 3: 210 },
    5: { 1: 190, 2: 210, 3: 230 },
    6: { 1: 230, 2: 245, 3: 260 },
  },
  "deep_cleaning": {
    1: { "studio": 170, 1: 190 },
    2: { 1: 210, 2: 225, 3: 240 },
    3: { 1: 220, 2: 240, 3: 255 },
    4: { 1: 250, 2: 270, 3: 290 },
    5: { 1: 270, 2: 290, 3: 310 },
    6: { 1: 310, 2: 325, 3: 340 },
  },
  "airbnb_cleaning": {
    1: { "studio": 130, 1: 150 },
    2: { 1: 170, 2: 185, 3: 205 },
    3: { 1: 185, 2: 200, 3: 215 },
    4: { 1: 210, 2: 230, 3: 250 },
    5: { 1: 230, 2: 250, 3: 270 },
    6: { 1: 260, 2: 280, 3: 300 },
  },
  "move_in_move_out_cleaning": {
    1: { "studio": 190, 1: 210 },
    2: { 1: 230, 2: 245, 3: 260 },
    3: { 1: 250, 2: 260, 3: 275 },
    4: { 1: 270, 2: 290, 3: 310 },
    5: { 1: 290, 2: 310, 3: 330 },
    6: { 1: 320, 2: 340, 3: 360 },
  },
}

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