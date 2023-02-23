from shop.extensions import db 
from shop.models.base import BaseModel

class Order(BaseModel):
    ___tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String)
    size = db.Column(db.String) 