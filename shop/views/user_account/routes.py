from flask import Blueprint, render_template, redirect, url_for, flash
from shop.views.user_account.forms import AccountForm, ConfirmForm
from shop.emails import send_email, create_key, confirm_key
from flask_login import login_required
from shop.views.filters.forms import ItemForm
from shop.models import User



user_account_blueprint = Blueprint(
    "user_account", __name__, template_folder="templates")

#email confiramtion
@user_account_blueprint.route("/confirm_email/<string:key>", methods=["GET", "POST"])
def confirm_email(key):
    email = confirm_key(key)
    user = User.query.filter_by(email=email).first()
    if user and not user.confirmed:
        user.confirmed = True
        user.save()
        return redirect(url_for('main.home'))
    else:
        flash ( "Wrong secret key or expired, or already confirmed" )
        
@user_account_blueprint.route("/my_account",  methods=["GET", "POST", "PUT"])
@login_required
def user_account():
    form = ItemForm()
    user = User.query.filter_by(email= User.email).first()
    user_form = AccountForm()
    conf_form = ConfirmForm()
    if conf_form.validate_on_submit():
        if user.confirmed == True:
            flash("Your mail is already confirmed")
        else:
            flash("You have been sent confirmation email, please check it before it expires!")

            key = create_key(user.email)
            html = render_template('authentication/_activation_message.html', key=key)
            send_email("Confirm your account", html, user.email)

    return render_template("user_account/account.html", userform=user_form, itemform = form, confirmform = conf_form)


