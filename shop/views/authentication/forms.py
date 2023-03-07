from wtforms.fields import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, equal_to, length
from flask_wtf import FlaskForm


class RegisterForm(FlaskForm):
    username = StringField("Enter your username", validators=[
        DataRequired(message="username is required")])
    email = EmailField("Enter your email", validators=[DataRequired(
        message="Email is required"), Email(message="Please enter valid email")])
    password = PasswordField("Enter password", validators=[
                             DataRequired(message="Password is required"),length(message = "Put min8 and max 16 symbols", min = 8, max=16) ])
    confirmation = PasswordField("Enter your password again", validators=[DataRequired("confirm password required"),
                                                                 equal_to("password", message="Passwords do not match")])
    submit = SubmitField()


class LoginForm(FlaskForm):
    username_or_email = StringField("Enter your username or email", validators=[
        DataRequired(message="username or email is required")])
    password = PasswordField("Enter your password",
                             validators=[DataRequired()])
    submit = SubmitField()
