from flask import Blueprint, render_template, redirect, url_for, flash
#from flask_login import current_user
from flask_login import login_required
from shop.models import Product
from shop.views.filters.forms import ItemForm
home_blueprint = Blueprint("main", __name__, template_folder="templates")

@home_blueprint.route("/", methods = ["GET", "POST"])
def home():
    product  = Product.query.all()
    form = ItemForm()
    if form.validate_on_submit():
        data = form.search.data
        print(data)
        
        if len(data) >= 1:
            product = Product.query.\
            filter(Product.name.contains(data)).all()
            return render_template ("home/home.html", itemform = form, products = product)
    return render_template("home/home.html", products = product, itemform = form)

@home_blueprint.route("/order/<int:product_id>", methods = ["GET", "POST"])
@login_required
def order( product_id = None):
    item  = Product.query.filter_by(id = product_id).first()

    item.quantity = int(item.quantity) - 1
    item.save()

    if item.quantity == 0:
        item.delete()
        item.save()
    flash("success")
    return redirect(url_for("main.home"))