from flask import Blueprint, render_template, redirect, url_for
from shop.views.authentication.forms import RegisterForm, LoginForm
from shop.models import User



authentication_blueprint = Blueprint("authentication", __name__, template_folder="templates")

@authentication_blueprint.route("/registration", methods=["GET", "POST"])
def registration():
    register_form = RegisterForm ()
    if register_form.validate_on_submit():
        user = User(username = register_form.username.data, email = register_form.email.data, password = register_form.password.data)
        user.create()
        user.save()
    else:
        print(register_form.errors)
    return render_template("authentication/registration.html", registerform = register_form)


