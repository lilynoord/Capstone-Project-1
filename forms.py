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
from wtforms.validators import DataRequired, optional
from wtforms.csrf.core import CSRFTokenField


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
        render_kw={
            "oninput": "update_ability_modifier(event)",
            "data-skill": "str-skill",
        },
    )
    dexterity = IntegerField(
        "Dexterity",
        validators=[DataRequired()],
        render_kw={
            "oninput": "update_ability_modifier(event)",
            "data-skill": "dex-skill",
        },
    )
    constitution = IntegerField(
        "Constitution",
        validators=[DataRequired()],
        render_kw={
            "oninput": "update_ability_modifier(event)",
            "data-skill": "con-skill",
        },
    )
    intelligence = IntegerField(
        "Intelligence",
        validators=[DataRequired()],
        render_kw={
            "oninput": "update_ability_modifier(event)",
            "data-skill": "int-skill",
        },
    )
    wisdom = IntegerField(
        "Wisdom",
        validators=[DataRequired()],
        render_kw={
            "oninput": "update_ability_modifier(event)",
            "data-skill": "wis-skill",
        },
    )
    charisma = IntegerField(
        "Charisma",
        validators=[DataRequired()],
        render_kw={
            "oninput": "update_ability_modifier(event)",
            "data-skill": "cha-skill",
        },
    )


class SavingThrows(FlaskForm):
    strength = IntegerField(
        "Strength",
        validators=[DataRequired()],
        render_kw={
            "class": "pico-override save-form str-skill",
        },
    )
    dexterity = IntegerField(
        "Dexterity",
        validators=[DataRequired()],
        render_kw={"class": "pico-override save-form dex-skill"},
    )
    constitution = IntegerField(
        "Constitution",
        validators=[DataRequired()],
        render_kw={"class": "pico-override save-form con-skill"},
    )
    intelligence = IntegerField(
        "Intelligence",
        validators=[DataRequired()],
        render_kw={"class": "pico-override save-form int-skill"},
    )
    wisdom = IntegerField(
        "Wisdom",
        validators=[DataRequired()],
        render_kw={"class": "pico-override save-form wis-skill"},
    )
    charisma = IntegerField(
        "Charisma",
        validators=[DataRequired()],
        render_kw={"class": "pico-override save-form cha-skill"},
    )


class SkillForms(FlaskForm):
    acrobatics = IntegerField(
        "Acrobatics",
        validators=[DataRequired()],
        render_kw={"class": "pico-override skill-form dex-skill"},
    )
    animal_handling = IntegerField(
        "Animal Handling",
        validators=[DataRequired()],
        render_kw={"class": "pico-override skill-form wis-skill"},
    )
    arcana = IntegerField(
        "Arcana",
        validators=[DataRequired()],
        render_kw={"class": "pico-override skill-form int-skill"},
    )
    athletics = IntegerField(
        "Athletics",
        validators=[DataRequired()],
        render_kw={"class": "pico-override skill-form str-skill"},
    )
    deception = IntegerField(
        "Deception",
        validators=[DataRequired()],
        render_kw={"class": "pico-override skill-form cha-skill"},
    )
    history = IntegerField(
        "History",
        validators=[DataRequired()],
        render_kw={"class": "pico-override skill-form int-skill"},
    )
    insight = IntegerField(
        "Insight",
        validators=[DataRequired()],
        render_kw={"class": "pico-override skill-form wis-skill"},
    )
    intimidation = IntegerField(
        "Intimidation",
        validators=[DataRequired()],
        render_kw={"class": "pico-override skill-form cha-skill"},
    )
    investigation = IntegerField(
        "Investigation",
        validators=[DataRequired()],
        render_kw={"class": "pico-override skill-form int-skill"},
    )
    medicine = IntegerField(
        "Medicine",
        validators=[DataRequired()],
        render_kw={"class": "pico-override skill-form wis-skill"},
    )
    nature = IntegerField(
        "Nature",
        validators=[DataRequired()],
        render_kw={"class": "pico-override skill-form int-skill"},
    )
    perception = IntegerField(
        "Perception",
        validators=[DataRequired()],
        render_kw={"class": "pico-override skill-form wis-skill"},
    )
    performance = IntegerField(
        "Performance",
        validators=[DataRequired()],
        render_kw={"class": "pico-override skill-form cha-skill"},
    )
    persuasion = IntegerField(
        "Persuasion",
        validators=[DataRequired()],
        render_kw={"class": "pico-override skill-form cha-skill"},
    )
    religion = IntegerField(
        "Religion",
        validators=[DataRequired()],
        render_kw={"class": "pico-override skill-form int-skill"},
    )
    sleight_of_hand = IntegerField(
        "Sleight of Hand",
        validators=[DataRequired()],
        render_kw={"class": "pico-override skill-form  dex-skill"},
    )
    stealth = IntegerField(
        "Stealth",
        validators=[DataRequired()],
        render_kw={"class": "pico-override skill-form  dex-skill"},
    )
    survival = IntegerField(
        "Survival",
        validators=[DataRequired()],
        render_kw={"class": "pico-override skill-form wis-skill"},
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
    damage_vulnerabilities = SelectMultipleField(
        "Damage Vulnerabilities", validators=[optional()]
    )
    damage_resistances = SelectMultipleField(
        "Damage Resistances", validators=[optional()]
    )
    damage_immunities = SelectMultipleField(
        "Damage Immunities", validators=[optional()]
    )
    condition_immunities = SelectMultipleField(
        "Condition Immunities", validators=[optional()]
    )


class AddPcForm(FlaskForm):
    header_forms = FormField(HeaderForms)
    ability_forms = FormField(AbilityForms)
    mid_forms = FormField(MidForms)
    proficiency_bonus = IntegerField(
        "proficiency_bonus", default=2, render_kw={"oninput": "update_skills(event)"}
    )
    saving_throws = FormField(SavingThrows)
    skill_forms = FormField(SkillForms)
    damage_forms = FormField(DamageForms)


# addnpcform


# ccounts+nameform
# cpcsform
# cnpcsform
# ccreaturesform

# updateentityform
