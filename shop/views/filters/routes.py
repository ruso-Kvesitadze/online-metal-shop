from flask import Blueprint, render_template, redirect, url_for, flash
#from flask_login import current_user
from shop.models import Product
from shop.views.filters.forms import ItemForm

filter_blueprint = Blueprint("filter", __name__, template_folder="templates")

@filter_blueprint.route("/shirts", methods = ["POST", "GET"])
def shirts():
    form = ItemForm()
    shirt = Product.query.filter_by(type = "Shirt")
    if form.validate_on_submit():
        data = form.search.data
        if len(data) >= 1:
            product = Product.query.\
            filter(Product.name.contains(data)).all()
            return render_template ("home/home.html", itemform = form, products = product)
    return render_template("filters/type.html", data = shirt, itemform = form)


@filter_blueprint.route("/hoodies", methods = ["POST", "GET"])
def hoodies():
    form = ItemForm()
    hoodie = Product.query.filter_by(type = "Hoodie")
    if form.validate_on_submit():
        data = form.search.data
        if len(data) >= 1:
            product = Product.query.\
            filter(Product.name.contains(data)).all()
            return render_template ("home/home.html", itemform = form, products = product)
    return render_template("filters/type.html", data = hoodie, itemform = form)

@filter_blueprint.route("/necklaces", methods = ["POST", "GET"])
def necklaces():
    form = ItemForm()
    necklace = Product.query.filter_by(type = "Necklace")
    if form.validate_on_submit():
        data = form.search.data
        if len(data) >= 1:
            product = Product.query.\
            filter(Product.name.contains(data)).all()
            return render_template ("home/home.html", itemform = form, products = product)
    return render_template("filters/type.html", data = necklace, itemform = form)

@filter_blueprint.route("/search", methods = ["POST", "GET"])
def search():
    form = ItemForm()
    print("fuck u ")
    if form.validate_on_submit():
        data = form.search.data
        print(data)

        if len(data) >= 1:
            product = Product.query.\
            filter(Product.name.contains(data)).all()
            return render_template ("home/home.html", itemform = form, products = product)
        return redirect("/")

