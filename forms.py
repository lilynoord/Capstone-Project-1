from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired


class SignInForm(FlaskForm):
    """Form for signing into or making a new (unsecured) account"""

    name = StringField("Username:", validators=[DataRequired()])
    password = PasswordField("Password (not secure!):", validators=[DataRequired()])
    new_account = BooleanField(
        "Create a new account?",
        default=False,
        render_kw={"role": "switch"},
    )


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
