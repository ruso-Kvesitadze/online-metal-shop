from flask import Blueprint, render_template, redirect, url_for, request, flash
from shop.extensions import mail
from shop.views.authentication.forms import RegisterForm, LoginForm, PasswordRecoveryForm, ResetPasswordForm
from shop.views.filters.forms import ItemForm
from shop.emails import  send_email, create_key, confirm_key
from flask_login import login_user, logout_user
from sqlalchemy import or_
from shop.models import User


authentication_blueprint = Blueprint(
    "authentication", __name__, template_folder="templates")

#registration
@authentication_blueprint.route("/registration", methods=["GET", "POST"])
def registration():
    register_form = RegisterForm()
    form = ItemForm()
    if register_form.validate_on_submit():

        if User.query.filter_by(email = register_form.email.data).first():
            flash("This email is already registered")
        elif User.query.filter_by(username = register_form.username.data).first():
            flash("This username is already registered, please enter something different")
        else:
            user = User(username=register_form.username.data,
                        email=register_form.email.data, password=register_form.password.data)
            user.create()
            user.save()
            flash("Succesfully Registered")
            flash("You have been sent confirmation email, please check it before it expires!")

            key = create_key(register_form.email.data)
            html = render_template('authentication/_activation_message.html', key=key)
            send_email("Confirm your account", html, register_form.email.data)
    else:
        print(register_form.errors)
    return render_template("authentication/registration.html", registerform=register_form, itemform = form)

#login
@authentication_blueprint.route("/login", methods=["GET", "POST"])
def login():
    form = ItemForm()
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter(or_(User.email ==login_form.username_or_email.data, User.username == login_form.username_or_email.data )).first()
        next = request.args.get("next")

        if user and user._check_password(login_form.password.data):
            login_user(user)
            if next:
                return redirect(url_for("user_account.user_account"))
            else:
                return redirect(url_for("main.home"))
        elif not user :
            flash ( "There's no account found with such email or username" )
        else:
            flash("Username, email or password is incorrect")
    else:
        print(login_form.errors)

    return render_template("authentication/login.html", loginform=login_form, itemform = form)

#email confiramtion
@authentication_blueprint.route("/confirm_email/<string:key>", methods=["GET", "POST"])
def confirm_email(key):
    email = confirm_key(key)
    user = User.query.filter_by(email=email).first()
    if user and not user.confirmed:
        user.confirmed = True
        user.save()
        return redirect(url_for('main.home'))
    else:
        flash ( "Wrong secret key or expired, or already confirmed" )

#forgot password
@authentication_blueprint.route("/forgot_password", methods=['GET', 'POST'])
def forgot_password():
    form = ItemForm()
    recovery_form = PasswordRecoveryForm()
    if recovery_form.validate_on_submit():
        user = User.query.filter_by(email=recovery_form.email.data).first()
        if user:
            user.reset_password = True
            reset_key = create_key(recovery_form.email.data)
            html = render_template('authentication/_reset_message.html', key=reset_key)
            send_email("Reset your password", html, recovery_form.email.data)
            user.save()
            flash( "You have been emailed password reset link" )
        elif not user:
            flash("User wasn't found with this email. Please register first!")
    return render_template('authentication/forgot_password.html', recoveryform=recovery_form, itemform = form)

#reset password
@authentication_blueprint.route("/reset_password/<string:key>", methods=['GET', 'POST'])
def reset_password(key):
    form = ItemForm()
    reset_form = ResetPasswordForm()
    email = confirm_key(key)
    user = User.query.filter_by(email=email).first()

    if not user: flash( "Wrong secret key or expired, or already confirmed" )
    if not user.reset_password: flash ( "Password already reset" )

    if reset_form.validate_on_submit():
        user.password = reset_form.password.data
        user.reset_password = False
        user.save()
        return redirect(url_for('authentication.login'))
    return render_template("authentication/reset_password.html", resetform=reset_form, itemform = form)

#logout
@authentication_blueprint.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.home")) 


