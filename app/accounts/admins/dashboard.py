from . import admin_bp
from flask import render_template


@admin_bp.route("/dashboard")
def admin_dashboard():
    return render_template("dashboards/admin.html", role="admin",)