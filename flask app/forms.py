from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

class userLoginForm(FlaskForm):
    username = StringField("User Name: ", validators=[DataRequired()])
    password = StringField("Password: ", validators=[DataRequired()])
    submit = SubmitField("Login")

# Form for stock search
class stockSearchForm(FlaskForm):
    searchQuery = StringField("Search Query")
    submit = SubmitField("Search")