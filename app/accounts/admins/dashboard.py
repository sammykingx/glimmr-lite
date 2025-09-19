from . import admin_bp
from flask import flash, render_template


@admin_bp.route("/dashboard")
def admin_dashboard():
    flash("Welcome to our admin dashboard!", "success")
    return render_template("dashboards/admin.html", role="admin",)