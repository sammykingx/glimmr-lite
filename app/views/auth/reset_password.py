from . import bp
from flask import current_app, flash, render_template, redirect, request, url_for
from app.decorators.verify_csrf_token import verify_csrf
from app.services.user_service import UserService
from app.constants.templates_map import Templates
from app.constants.email_subjects import EmailHeaders
from app.constants.token_purposes import TokenPurposes

account_manager = UserService()

@bp.route("/recover-account", methods=["GET", "POST"])
@verify_csrf
def password_reset_link():
    template = Templates.Auth.FORGOT_PASSWORD
    message = None
    category = "info"

    if request.method == "POST":
        email = request.form.get("email")
        user = account_manager.get_user("email", email)

        if not user:
            message = {
                "title": "Email Sent",
                "message": "Recovery instructions sent to user (if account exists).",
            }
        else:
            reset_token = account_manager.save_user_token(user)
            is_sent = account_manager.send_user_token(
                user=user,
                template_name=Templates.Emails.PASSWORD_RESET,
                token_purpose=TokenPurposes.PASSWORD_RESET,
                token=reset_token,
                subject=EmailHeaders.Auth.PASSWORD_RESET,
            )

            if is_sent:
                message = {
                    "title": "Reset Link Sent",
                    "message": "Check your email for reset instructions."
                }
                category = "success"
            else:
                message = {
                    "title": "Service Unavailable",
                    "message": "Email service unavailable. Please try again later."
                }
                category = "error"

        flash(message, category)

    return render_template(template)

@bp.route("/reset-password", methods=["GET", "POST"])
@verify_csrf
def reset_password():
    template = Templates.Auth.RESET_PASSWORD
    verf_token = request.args.get("verf_id")
    token_data = account_manager.verify_token(verf_token, purpose="password reset")
    
    if not token_data:
        print("NO/INVALID REQUEST TOKEN")
        flash({
            "title": "Link Not Working",
            "message": "It looks like this reset link has expired or isn’t valid anymore",
            }, "warning")
        return render_template(template, disable_input=True)
    
    if request.method == "POST":
        form_data = request.form.to_dict()
        user = account_manager.get_user("reset_token", token_data.get("token"))
        user.hash_pwd(form_data.get("password"))
        account_manager.update_user(user, password=form_data.get("password"))
        return redirect(url_for("auth.user_checkpiont"))
        
    # GET Request
    return render_template(template)