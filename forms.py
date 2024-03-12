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
    RadioField,
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
    strength = IntegerField(
        "Strength",
        validators=[DataRequired()],
        render_kw={"oninput": "update_ability_modifier(event)"},
    )
    dexterity = IntegerField(
        "Dexterity",
        validators=[DataRequired()],
        render_kw={"oninput": "update_ability_modifier(event)"},
    )
    constitution = IntegerField(
        "Constitution",
        validators=[DataRequired()],
        render_kw={"oninput": "update_ability_modifier(event)"},
    )
    intelligence = IntegerField(
        "Intelligence",
        validators=[DataRequired()],
        render_kw={"oninput": "update_ability_modifier(event)"},
    )
    wisdom = IntegerField(
        "Wisdom",
        validators=[DataRequired()],
        render_kw={"oninput": "update_ability_modifier(event)"},
    )
    charisma = IntegerField(
        "Charisma",
        validators=[DataRequired()],
        render_kw={"oninput": "update_ability_modifier(event)"},
    )


class SavingThrows(FlaskForm):
    strength = IntegerField(
        "Strength",
        validators=[DataRequired()],
        render_kw={
            "class": "save-form",
        },
    )
    dexterity = IntegerField(
        "Dexterity", validators=[DataRequired()], render_kw={"class": "save-form"}
    )
    constitution = IntegerField(
        "Constitution", validators=[DataRequired()], render_kw={"class": "save-form"}
    )
    intelligence = IntegerField(
        "Intelligence", validators=[DataRequired()], render_kw={"class": "save-form"}
    )
    wisdom = IntegerField(
        "Wisdom", validators=[DataRequired()], render_kw={"class": "save-form"}
    )
    charisma = IntegerField(
        "Charisma", validators=[DataRequired()], render_kw={"class": "save-form"}
    )


class SkillForms(FlaskForm):
    acrobatics = IntegerField(
        "Acrobatics", validators=[DataRequired()], render_kw={"class": "skill-form"}
    )
    animal_handling = IntegerField(
        "Animal Handling",
        validators=[DataRequired()],
        render_kw={"class": "skill-form"},
    )
    arcana = IntegerField(
        "Arcana", validators=[DataRequired()], render_kw={"class": "skill-form"}
    )
    athletics = IntegerField(
        "Athletics", validators=[DataRequired()], render_kw={"class": "skill-form"}
    )
    deception = IntegerField(
        "Deception", validators=[DataRequired()], render_kw={"class": "skill-form"}
    )
    history = IntegerField(
        "History", validators=[DataRequired()], render_kw={"class": "skill-form"}
    )
    insight = IntegerField(
        "Insight", validators=[DataRequired()], render_kw={"class": "skill-form"}
    )
    intimidation = IntegerField(
        "Intimidation", validators=[DataRequired()], render_kw={"class": "skill-form"}
    )
    investigation = IntegerField(
        "Investigation", validators=[DataRequired()], render_kw={"class": "skill-form"}
    )
    medicine = IntegerField(
        "Medicine", validators=[DataRequired()], render_kw={"class": "skill-form"}
    )
    nature = IntegerField(
        "Nature", validators=[DataRequired()], render_kw={"class": "skill-form"}
    )
    perception = IntegerField(
        "Perception", validators=[DataRequired()], render_kw={"class": "skill-form"}
    )
    performance = IntegerField(
        "Performance", validators=[DataRequired()], render_kw={"class": "skill-form"}
    )
    persuasion = IntegerField(
        "Persuasion", validators=[DataRequired()], render_kw={"class": "skill-form"}
    )
    religion = IntegerField(
        "Religion", validators=[DataRequired()], render_kw={"class": "skill-form"}
    )
    sleight_of_hand = IntegerField(
        "Sleight of Hand",
        validators=[DataRequired()],
        render_kw={"class": "skill-form"},
    )
    stealth = IntegerField(
        "Stealth", validators=[DataRequired()], render_kw={"class": "skill-form"}
    )
    survival = IntegerField(
        "Survival", validators=[DataRequired()], render_kw={"class": "skill-form"}
    )


class HeaderForms(FlaskForm):
    character_name = StringField(
        "Name:",
        validators=[DataRequired()],
        render_kw={"Placeholder": "Character Name"},
    )
    player_name = StringField("Player Name", render_kw={"Placeholder": "Player Name"})
    level = IntegerField(
        "Level", validators=[DataRequired()], render_kw={"Placeholder": "Level"}
    )
    character_class = SelectField(
        "Class", validators=[DataRequired()], render_kw={"aria-label": "Class"}
    )
    alignment = SelectField("Alignment", render_kw={"Placeholder": "Alignment"})
    size = SelectField(
        "Experience Points", render_kw={"Placeholder": "Experience Points"}
    )
    creature_type = StringField(
        "Race", validators=[DataRequired()], render_kw={"Placeholder": "Character Race"}
    )


class MidForms(FlaskForm):
    armor_class = IntegerField("Armor Class", validators=[DataRequired()])
    speed = IntegerField("Speed", validators=[DataRequired()])
    hit_point_maximum = IntegerField("Hit Point Maximum", validators=[DataRequired()])
    hit_dice_count = IntegerField("", validators=[DataRequired()])
    hit_dice_type = IntegerField("", validators=[DataRequired()])


class DamageForms(FlaskForm):
    damage_vulnerabilities = SelectMultipleField("Damage Vulnerabilities")
    damage_resistances = SelectMultipleField("Damage Resistances")
    damage_immunities = SelectMultipleField("Damage Immunities")
    condition_immunities = SelectMultipleField("Condition Immunities")


class AddPcForm(FlaskForm):
    header_forms = FormField(HeaderForms)
    ability_forms = FormField(AbilityForms)
    mid_forms = FormField(MidForms)
    proficiency_bonus = IntegerField("proficiency_bonus", default=2)
    inspiration = IntegerField("Inspiration", default=0)
    saving_throws = FormField(SavingThrows)
    skill_forms = FormField(SkillForms)
    damage_forms = FormField(DamageForms)


# addnpcform


# ccounts+nameform
# cpcsform
# cnpcsform
# ccreaturesform

# updateentityform
