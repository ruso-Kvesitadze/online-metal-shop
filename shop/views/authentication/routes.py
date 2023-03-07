from flask import Blueprint, render_template, redirect, url_for, request, flash
from shop.views.authentication.forms import RegisterForm, LoginForm
from flask_login import login_user, logout_user
from sqlalchemy import or_
from shop.models import User


authentication_blueprint = Blueprint(
    "authentication", __name__, template_folder="templates")


@authentication_blueprint.route("/registration", methods=["GET", "POST"])
def registration():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        if User.query.filter_by(email=register_form.email.data).first():
            flash("This email is already registered")
        if User.query.filter_by(username=register_form.username.data).first():
            flash("This username is already registered, please enter something different")
        else:
            user = User(username=register_form.username.data,
                        email=register_form.email.data, password=register_form.password.data)
            user.create()
            user.save()
            flash("Succesfully Registered")
    else:
        print(register_form.errors)
    return render_template("authentication/registration.html", registerform=register_form)


@authentication_blueprint.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter(or_(User.email ==login_form.username_or_email.data, User.username == login_form.username_or_email.data )).first()
        next = request.args.get("next")
        if user and user._check_password(login_form.password.data):
            print(next)
            login_user(user)
        return redirect(url_for('main.home'))
    else:
        print(login_form.errors)

    return render_template("authentication/login.html", loginform=login_form)

@authentication_blueprint.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.home"))
