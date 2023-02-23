from shop.extensions import db 
from shop.models.base import BaseModel

class User(BaseModel):
    __tablename__ = "registered_users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    mobile_number = db.Column(db.String)
    mail = db.Column(db.String)
    password = db.Column(db.String)