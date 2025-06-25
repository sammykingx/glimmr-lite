from app import create_app
from flask import render_template

app = create_app()

# @app.after_request
# def add_security_headers(response):
#     response.headers["X-Frame-Options"] = "DENY"
#     response.headers["X-Content-Type-Options"] = "nosniff"
#     response.headers["Content-Security-Policy"] = "default-src 'self'"
#     return response

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
