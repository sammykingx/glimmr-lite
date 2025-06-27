import pytz


# Define the timezone for Toronto
TORONRO_TZ = pytz.timezone("America/Toronto")


ALLOWED_SERVICE_CATEGORY = [
    "residential",
    "commercial",
    "industrial",
]

ALLOWED_SERVICE_TYPE = [
    "standard-cleaning",
    "deep-cleaning",
    "move-in-move-out-cleaning",
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
    "oven-cleaning",
    "fridge-cleaning",
    "laundry",
    "ironing",
    "carpet-shampooing",
    "window-washing",
]