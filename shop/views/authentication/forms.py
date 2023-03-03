from wtforms.fields import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, equal_to
from flask_wtf import FlaskForm


class RegisterForm(FlaskForm):
    username = StringField("Enter your username", validators=[
        DataRequired(message="username is required")])
    email = EmailField("Enter your email", validators=[DataRequired(
        message="Email is required"), Email(message="Please enter valid email")])
    password = PasswordField("Enter password", validators=[
                             DataRequired(message="Password is required")])
    confirmation = PasswordField("Enter your password again", validators=[DataRequired("confirm password required"),
                                                                 equal_to("password", message="Passwords do not match")])
    submit = SubmitField()


class LoginForm(FlaskForm):
    username = StringField("Enter your username", validators=[
        DataRequired(message="username is required")])
    email = StringField("Enter your mail", validators=[
                        DataRequired(message="You can't log in without mail")])
    password = PasswordField("Enter your password",
                             validators=[DataRequired()])
    submit = SubmitField()
