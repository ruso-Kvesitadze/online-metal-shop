from wtforms.fields import StringField, SubmitField
from flask_wtf import FlaskForm

class ItemForm(FlaskForm):

    search = StringField("Search")
    submit = SubmitField("Search")