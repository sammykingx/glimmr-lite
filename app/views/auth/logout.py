from . import bp
from flask import redirect, url_for
from flask_login import logout_user, login_required


@bp.route("/logout")
@login_required
def user_logout():
    logout_user()
    return redirect(url_for("auth.user_login"))