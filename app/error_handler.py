from flask import current_app, flash, redirect, request, render_template, url_for
from flask_login import current_user
from app.constants.templates_map import Templates
import traceback


def bad_request(error):
    if current_user.is_authenticated:
        flash(
            {
                "title": "A Little Mix-Up",
                "message": "We couldn’t process that request, maybe give it another try?",
            }, "info"
        )
        return redirect(url_for("accounts.dashboard"))
    
    return render_template(Templates.Errors.ERROR_400)


def unauthorized_request(error):
    if current_user.is_authenticated:
        flash(
            {
                "title": "You’re Not Signed In",
                "message": "Please log in to continue, we’ll keep your spot shining for you",
            }, "info"
        )
        return redirect(url_for("accounts.dashboard"))
    
    return render_template(Templates.Errors.ERROR_401)


def forbidden_request(error):
    if current_user.is_authenticated:
        flash(
            {
                "title": "Access Restricted",
                "message": "Looks like that area is off-limits, only authorized personnels are allowed.",
            }, "info"
        )
        return redirect(url_for("accounts.dashboard"))
    
    return render_template(Templates.Errors.ERROR_403)


def page_not_found(error):
    if current_user.is_authenticated:
        flash(
            {
                "title": "Resource Not Found",
                "message": "Oops! Looks like you took a wrong turn earlier.",
            }, "info"
        )
        return redirect(url_for("accounts.dashboard"))
    
    return render_template(Templates.Errors.ERROR_404)


def method_not_allowed(error):
    if current_user.is_authenticated:
        flash(
            {
                "title": "Wrong Approach",
                "message": "That action isn’t allowed here, maybe try a different route",
            }, "info"
        )
        return redirect(url_for("accounts.dashboard"))
    
    return render_template(Templates.Errors.ERROR_405)


def internal_server(error):
    current_app.logger.error(
        f"[500 ERROR] User: {getattr(current_user, 'email', 'Anonymous')} | "
        f"Path: {request.path} | Method: {request.method} | "
        f"Type: {type(error).__name__} | Message: {error}\n{traceback.format_exc()}"
    )
    
    if current_user.is_authenticated:
        flash(
            {
                "title": "Taking a Quick Polish",
                "message": "Even the shiniest systems need a quick dust-off, hang tight cause e're on it.",
            }, "info"
        )
        return redirect(url_for("accounts.dashboard"))
     
    return render_template(Templates.Errors.ERROR_500)

