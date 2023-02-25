from flask.cli import with_appcontext
import click
from shop.extensions import db
from shop.models import Product
from shop.data import products


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
    for product in products:
        product_info = Product(type=product.get("type"), name=product.get("name"), quantity=product.get(
            "quantity"), price=product.get("price"), img_link=product.get("img-link"))
        product_info.create()
    product_info.save()
    click.echo("Finished populating db")
