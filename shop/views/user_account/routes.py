from flask import Blueprint, render_template, redirect, url_for, flash
from shop.views.user_account.forms import AccountForm
from shop.emails import send_email, create_key, confirm_key
from flask_login import login_required
from shop.views.filters.forms import ItemForm


user_account_blueprint = Blueprint(
    "user_account", __name__, template_folder="templates")


@user_account_blueprint.route("/my_account",  methods=["GET", "POST", "PUT"])
@login_required
def user_account():
    form = ItemForm()
    user_form = AccountForm()
    return render_template("user_account/account.html", userform=user_form, itemform = form)
