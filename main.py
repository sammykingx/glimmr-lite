from app import create_app
from flask import render_template, redirect, request, url_for
from flask_login import current_user
from app.constants.services import ALLOWED_SERVICE, ALLOWED_SERVICE_ADDONS

app = create_app()

@app.context_processor
def inject_globals():
    return dict(user=current_user)

@app.before_request
def enforce_onboarding():
    if current_user.is_authenticated:
        exempt_routes = {
            "accounts.onboarding_user",
            "auth.user_logout", 
            "static"}
        if (not current_user.onboarding_complete
            and request.endpoint not in exempt_routes
            and not request.endpoint.startswith("static")):
            return redirect(url_for("accounts.onboarding_user"))


@app.route("/")
def index():
    return render_template(
        "index.html",
        categories=ALLOWED_SERVICE.keys(),
        addons=ALLOWED_SERVICE_ADDONS,
    )

@app.route("/coming-soon")
def coming_soon():
    return render_template(
        "pages/system/under-construction.html",
        role="admin",
    )

if __name__ == "__main__":
    app.run()
