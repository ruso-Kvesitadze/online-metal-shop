from shop.extensions import db 
from shop.models.base import BaseModel

class Shirt(BaseModel):
    __tablename__ = "shirts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    quantity  = db.Column(db.Integer)
    price = db.Column(db.Integer)
    img_link = db.Column(db.String)

class Necklace(BaseModel):
    __tablename__ = "necklaces"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    quantity  = db.Column(db.Integer)
    price = db.Column(db.Integer)
    img_link = db.Column(db.String)

class Hoodie(BaseModel):
    __tablename__ = "hoodies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    quantity  = db.Column(db.Integer)
    price = db.Column(db.Integer)
    img_link = db.Column(db.String)