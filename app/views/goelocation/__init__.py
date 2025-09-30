from flask import Blueprint, render_template

geo_bp = Blueprint("geolocation", __name__, url_prefix="/geolocation")

@geo_bp.route("/track")
def track():
    return render_template("pages/system/under-construction.html", role="admin", feature="Geolocation")