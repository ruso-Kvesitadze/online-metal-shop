from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user

home_blueprint = Blueprint("home", __name__, template_folder="templates")

@home_blueprint.route("/home")
def home():
    return render_template("home/home.html")

# @main_blueprint.route("/admin")
# def admin_pannel():
#     if current_user.has_roles("admin"):
#         print(current_user.has_roles("admin"))
#         return "you are admin"
#     else:
#         print(current_user.has_roles("admin"))
#         return redirect(url_for("main.home"))