from flask_wtf import FlaskForm
from wtforms import (
    SelectField,
    StringField,
    PasswordField,
    BooleanField,
    IntegerField,
    FormField,
    TextAreaField,
    SelectMultipleField,
)
from wtforms.validators import DataRequired


class SignInForm(FlaskForm):
    """Form for signing into or making a new (unsecured) account"""

    name = StringField(
        "Username:",
        validators=[DataRequired()],
    )
    password = PasswordField("Password (not secure!):", validators=[DataRequired()])
    new_account = BooleanField(
        "Create a new account?",
        default=False,
        render_kw={"role": "switch"},
    )


class NewGameForm(FlaskForm):
    name = StringField("Game Name:", validators=[DataRequired()])


# addcreatureform


class AbilityForms(FlaskForm):
    strength = IntegerField("Strength", validators=[DataRequired()], render_kw={})
    dexterity = IntegerField("Dexterity", validators=[DataRequired()], render_kw={})
    constitution = IntegerField(
        "Constitution", validators=[DataRequired()], render_kw={}
    )
    intelligence = IntegerField(
        "Intelligence", validators=[DataRequired()], render_kw={}
    )
    wisdom = IntegerField("Wisdom", validators=[DataRequired()], render_kw={})
    charisma = IntegerField("Charisma", validators=[DataRequired()], render_kw={})


class SavingThrows(FlaskForm):
    strength = IntegerField("Strength", validators=[DataRequired()], render_kw={})
    dexterity = IntegerField("Dexterity", validators=[DataRequired()], render_kw={})
    constitution = IntegerField(
        "Constitution", validators=[DataRequired()], render_kw={}
    )
    intelligence = IntegerField(
        "Intelligence", validators=[DataRequired()], render_kw={}
    )
    wisdom = IntegerField("Wisdom", validators=[DataRequired()], render_kw={})
    charisma = IntegerField("Charisma", validators=[DataRequired()], render_kw={})


class SkillForms(FlaskForm):
    acrobatics = IntegerField("Acrobatics", validators=[DataRequired()], render_kw={})
    animal_handling = IntegerField(
        "Animal Handling", validators=[DataRequired()], render_kw={}
    )
    arcana = IntegerField("Arcana", validators=[DataRequired()], render_kw={})
    athletics = IntegerField("Athletics", validators=[DataRequired()], render_kw={})
    deception = IntegerField("Deception", validators=[DataRequired()], render_kw={})
    history = IntegerField("History", validators=[DataRequired()], render_kw={})
    insight = IntegerField("Insight", validators=[DataRequired()], render_kw={})
    intimidation = IntegerField(
        "Intimidation", validators=[DataRequired()], render_kw={}
    )
    investigation = IntegerField(
        "Investigation", validators=[DataRequired()], render_kw={}
    )
    medicine = IntegerField("Medicine", validators=[DataRequired()], render_kw={})
    nature = IntegerField("Nature", validators=[DataRequired()], render_kw={})
    perception = IntegerField("Perception", validators=[DataRequired()], render_kw={})
    performance = IntegerField("Performance", validators=[DataRequired()], render_kw={})
    persuasion = IntegerField("Persuasion", validators=[DataRequired()], render_kw={})
    religion = IntegerField("Religion", validators=[DataRequired()], render_kw={})
    sleight_of_hand = IntegerField(
        "Sleight of Hand", validators=[DataRequired()], render_kw={}
    )
    stealth = IntegerField("Stealth", validators=[DataRequired()], render_kw={})
    survival = IntegerField("Survival", validators=[DataRequired()], render_kw={})


class HeaderForms(FlaskForm):
    character_name = StringField(
        "Name:",
        validators=[DataRequired()],
        render_kw={"Placeholder": "Character Name"},
    )
    player_name = StringField("Class", render_kw={"Placeholder": "Player Name"})
    level = IntegerField(
        "Level", validators=[DataRequired()], render_kw={"Placeholder": "Level"}
    )
    character_class = SelectField(
        "Class", validators=[DataRequired()], render_kw={"Placeholder": "Class"}
    )
    alignment = SelectField("Alignment", render_kw={"Placeholder": "Alignment"})
    experience = IntegerField(
        "Experience Points", render_kw={"Placeholder": "Experience Points"}
    )


class MidForms(FlaskForm):
    armor_class = IntegerField("Armor Class", validators=[DataRequired()])
    initiative = IntegerField("Initiative Bonus", validators=[DataRequired()])
    speed = IntegerField("Speed", validators=[DataRequired()])
    hit_point_maximum = IntegerField("Hit Point Maximum", validators=[DataRequired()])
    hit_dice_count = IntegerField("", validators=[DataRequired()])
    hit_dice_type = IntegerField("", validators=[DataRequired()])


class TraitsForm(FlaskForm):
    personality_traits = TextAreaField("")
    ideals = TextAreaField("")
    bonds = TextAreaField("")
    flaws = TextAreaField("")


class DamageForms(FlaskForm):
    damage_vulnerabilities = SelectMultipleField("Damage Vulnerabilities")
    damage_resistances = SelectMultipleField("Damage Resistances")
    damage_immunities = SelectMultipleField("Damage Immunities")
    condition_immunities = SelectMultipleField("Condition Immunities")


class AddPcForm(FlaskForm):
    header_forms = FormField(HeaderForms)
    ability_forms = FormField(AbilityForms)
    creature_type = StringField("Race", validators=[DataRequired()])
    proficiency_bonus = IntegerField("proficiency_bonus", default=2)
    saving_throws = FormField(SavingThrows)
    skill_forms = FormField(SkillForms)
    damage_forms = FormField(DamageForms)


# addnpcform


# ccounts+nameform
# cpcsform
# cnpcsform
# ccreaturesform

# updateentityform
