ALLOWED_SERVICE = {
    "residential_cleaning": {
        "type": "list",
        "options": [
            "house_cleaning",
            "deep_cleaning",
            "move_in_move_out_cleaning",
            "airbnb_cleaning",
        ],
    },
    "commercial_cleaning": {
        "type": "size_based",
        "sizes": {
            "small": {"label": "<2,000sqft", "multiplier": 0.2, "amount": 400},
            "medium": {
                "label": "2,000sqft - 5,000sqft",
                "multiplier": 0.18,
                "amount": 900,
            },
            "large": {
                "label": "5,000sqft - 10,000sqft",
                "multiplier": 0.16,
                "amount": 1600,
            },
            "custom": {"label": ">10,000sqft"},
        },
    },
    "church_cleaning": {
        "type": "size_based",
        "sizes": {
            "small": {"label": "<3,000sqft", "amount": 180},
            "medium": {"label": "3,000sqft - 6,000sqft", "amount": 300},
            "large": {"label": ">6,000sqft", "amount": 500},
        },
    },
    "child_care": {
        "type": "size_based",
        "sizes": {
            "small": {"label": "<2,000sqft", "amount": 250},
            "medium": {"label": "2,000sqft - 5,000sqft", "amount": 350},
            "large": {"label": ">5,000sqft", "amount": 500},
        },
    },
    "gym": {
        "type": "size_based",
        "sizes": {
            "small": {"label": "<3,000sqft", "amount": 300},
            "medium": {"label": "3,000sqft - 7,000sqft", "amount": 450},
            "large": {"label": ">7,000sqft", "amount": 650},
        },
    },
    "salon_cleaning": {
        "type": "size_based",
        "sizes": {
            "small": {"label": "<1,500sqft", "amount": 150},
            "medium": {"label": "1,500sqft - 3,000sqft", "amount": 200},
            "large": {"label": ">3,000sqft", "amount": 300},
        },
    },
    "retail_cleaning": {
        "type": "size_based",
        "sizes": {
            "small": {"label": "<3,000sqft", "amount": 200},
            "medium": {"label": "2,000sqft - 5,000sqft", "amount": 350},
            "large": {"label": ">5,000sqft", "amount": 500},
        },
    },
    "office_cleaning": {
        "type": "size_based",
        "sizes": {
            "small": {"label": "<2,000sqft", "amount": 180},
            "medium": {"label": "2,000sqft - 5,000sqft", "amount": 300},
            "large": {"label": ">5,000sqft", "amount": 500},
        },
    },
}

ALLOWED_FREQUENCIES = ["one_off", "weekly", "bi_weekly", "monthly"]

ALLOWED_SERVICE_ADDONS = [
    {"name": "interior window cleaning", "amount": 50, "max": 10},
    {"name": "blinds dusting", "amount": 20, "max": 10},
    {"name": "oven cleaning", "amount": 30},
    {"name": "fridge cleaning", "amount": 25},
    {"name": "laundry", "amount": 35, "max": "2 loads"},
    {"name": "Basement cleaning", "amount": 70},
    {"name": "garage cleaning", "amount": 60},
    {"name": "porch/balcony cleaning", "amount": 25},
    {"name": "driveway sweeping", "amount": 30},
]
