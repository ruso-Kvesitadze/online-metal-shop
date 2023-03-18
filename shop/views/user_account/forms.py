from wtforms.fields import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, equal_to, length
from flask_wtf import FlaskForm


class AccountForm(FlaskForm):
    username = StringField("Your username")
    email = EmailField("Your email")
    mobile_number = StringField("Your mobile number")
    card_info = StringField("Your card number")
    submit = SubmitField()
