from app import create_app
from flask import render_template
from flask_login import current_user
from app.constants.services import ALLOWED_SERVICE, ALLOWED_SERVICE_ADDONS

app = create_app()

@app.context_processor
def inject_globals():
    return dict(user=current_user)

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
