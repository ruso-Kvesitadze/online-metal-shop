from flask.cli import with_appcontext
import click
from shop.extensions import db
from shop.models import Product, User
from shop.data import products, admins


@click.command("init_db")
@with_appcontext
def init_db():
    click.echo("Creating db")
    db.drop_all()
    db.create_all()
    click.echo("Finished Creating db")


@click.command("populate_db")
@with_appcontext
def populate_db():
    click.echo("populating db")
    # populating "products" table
    click.echo("populating products table")
    for product in products:
        product_info = Product(type=product.get("type"), name=product.get("name"), quantity=product.get(
            "quantity"), price=product.get("price"), img_link=product.get("img-link"))
        product_info.create()
    product_info.save()
    click.echo("finished populating products table")
    click.echo("populating admin users")
    for admin in admins:
        user_admin = User(username = admin.get("username"), email = admin.get("email"), password = admin.get("password"), roles = admin.get("role"), card_info = admin.get("card_info"), mobile_number = admin.get("mobile_number"))
        user_admin.create()
    user_admin.save()
    click.echo("finished creating admin users")
    click.echo("Finished populating db")
