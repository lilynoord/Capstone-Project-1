from flask_wtf import FlaskForm
from wtforms import SelectField, StringField
from wtforms.validators import DataRequired


class SignInForm(FlaskForm):
    """Form for signing into or making a new (unsecured) account"""

    name = StringField("Username:", validators=[DataRequired()])


class NewGameForm(FlaskForm):
    name = StringField("Game Name:", validators=[DataRequired()])


# addcreatureform
# addpcform
# addnpcform


# ccounts+nameform
# cpcsform
# cnpcsform
# ccreaturesform

# updateentityform
