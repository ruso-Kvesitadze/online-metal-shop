from shop.extensions import db 
from shop.models.base import BaseModel
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(BaseModel, UserMixin):
    __tablename__ = "registered_users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique = True, nullable = False)
    email = db.Column(db.String, unique = True, nullable = False)
    _password = db.Column("password",db.String)
    roles = db.Column(db.String)
    card_info = db.Column(db.String)
    mobile_number = db.Column(db.String)

    def _get_password(self):
        return self._password
    def _set_password(self, password):
        self._password = generate_password_hash(password)
    def _check_password(self,password):
        return check_password_hash(self.password, password)
    
    password = db.synonym("_password", descriptor = property(_get_password, _set_password))