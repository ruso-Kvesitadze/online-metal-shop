from flask.cli import with_appcontext
import click
from shop.extensions import db
from shop.models.user import User
from shop.models.orders import Order
from shop.models.products import Shirt, Necklace, Hoodie
from shop.data import shirts, necklaces, hoodies


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
    #populating shirts table 
    for shirt in shirts:
        info = Shirt(name = shirt.get("name"), quantity = shirt.get("quantity"), price =  shirt.get("price"), img_link = shirt.get("img-link"))
        info.create()
    info.save()
    click.echo("Finished populating 'shirts' table")

    #populating necklaces table 
    for necklace in necklaces:
        info = Necklace(name = necklace.get("name"), quantity = necklace.get("quantity"), price =  necklace.get("price"), img_link = necklace.get("img-link"))
        info.create()
    info.save()
    click.echo("Finished populating 'necklaces' table")

    #populating hoodies table 
    for hoodie in hoodies:
        info = Hoodie(name = hoodie.get("name"), quantity = hoodie.get("quantity"), price =  hoodie.get("price"), img_link = hoodie.get("img-link"))
        info.create()
    info.save()
    click.echo("Finished populating 'hoodies' table")
    click.echo("Finished populating db")


