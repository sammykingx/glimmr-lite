from . import accounts_bp
from flask import render_template, Response


@accounts_bp.route("/view-clients")
def view_clients() -> Response:
    """
    Clients view for user accounts, accessible by admins and managers only.
    
    :return: HTTP Response containing rendered HTML template
    """
    return render_template("pages/system/under-construction.html", role="admin",)


@accounts_bp.route("/view-staffs")
def view_staffs() -> Response:
    """
    Staffs view for user accounts, accessible by admins and managers only.
    
    :return: HTTP Response containing rendered HTML template
    """
    return render_template("pages/system/under-construction.html", role="admin",)