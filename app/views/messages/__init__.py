from flask import Blueprint, render_template


msg_bp = Blueprint("messages", __name__, url_prefix="/messages")

@msg_bp.route("/inbox")
def inbox():
    return render_template("pages/system/under-construction.html", role="admin", feature="Messages")