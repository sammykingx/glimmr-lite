from flask import Blueprint, render_template

pay_bp = Blueprint("payments", __name__, url_prefix="/payments")

@pay_bp.route("/process-payment")
def process_payment():
    return render_template("pages/system/under-construction.html", role="admin",)