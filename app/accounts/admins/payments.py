from . import admin_bp
from flask import render_template


@admin_bp.route("view-payments")
def view_payments():
    return render_template(
        "pages/system/under-construction.html",
        role="admin",
    )