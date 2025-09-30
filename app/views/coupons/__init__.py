from flask import Blueprint, render_template

coupons_bp = Blueprint("coupons", __name__, url_prefix="/coupons")

@coupons_bp.route("/manage-coupons")
def manage_coupons():
    return render_template("pages/system/under-construction.html", role="admin",)