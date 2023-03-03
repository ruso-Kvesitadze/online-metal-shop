from flask import Blueprint, render_template, redirect, url_for
#from flask_login import current_user
from shop.models import Product
home_blueprint = Blueprint("main", __name__, template_folder="templates")

@home_blueprint.route("/", methods = ["GET", "POST"])
def home():
    product  = Product.query.all()
    print(f"{product} hi")
    return render_template("home/home.html", products = product)

# @main_blueprint.route("/admin")
# def admin_pannel():
#     if current_user.has_roles("admin"):
#         print(current_user.has_roles("admin"))
#         return "you are admin"
#     else:
#         print(current_user.has_roles("admin"))
#         return redirect(url_for("main.home"))