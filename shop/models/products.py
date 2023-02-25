from shop.extensions import db 
from shop.models.base import BaseModel

class Product(BaseModel):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String) 
    name = db.Column(db.String)
    quantity  = db.Column(db.Integer)
    price = db.Column(db.Integer)
    img_link = db.Column(db.String)
