from app import create_app
from flask import render_template
from app.constants import ALLOWED_SERVICE, ALLOWED_SERVICE_ADDONS

app = create_app()

@app.route('/')
def index():
    return render_template(
        'index.html',
        categories=ALLOWED_SERVICE.keys(),
        addons=ALLOWED_SERVICE_ADDONS)

if __name__ == "__main__":
    app.run()
