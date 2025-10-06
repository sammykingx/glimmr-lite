from . import booking_bp
from flask import render_template
from app.constants.templates_map import Templates

@booking_bp.route("/services")
def service_catalog():
    return render_template(Templates.SERVICE_LISTING)