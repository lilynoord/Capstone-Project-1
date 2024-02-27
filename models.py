from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """"""

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class Game(db.Model):
    """"""

    __tablename__ = "games"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class GameMonster(db.Model):
    """"""

    __tablename__ = "games_monsters"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class GamePc(db.Model):
    """"""

    __tablename__ = "games_pcs"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class GameNpc(db.Model):
    """"""

    __tablename__ = "games_npcs"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class Combat(db.Model):
    """"""

    __tablename__ = "combats"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class CombatMonster(db.Model):
    """"""

    __tablename__ = "combats_monsters"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class CombatPc(db.Model):
    """"""

    __tablename__ = "combats_pcs"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class CombatNpc(db.Model):
    """"""

    __tablename__ = "combats_npcs"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class Monster(db.Model):
    """"""

    __tablename__ = "monsters"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    slug = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    creature_type = db.Column(db.Text, nullable=False)
    alignment = db.Column(db.Text, nullable=False)
    armor_class = db.Column(db.Integer, nullable=False)
    armor_desc = db.Column(db.Text, nullable=False)
    max_hit_points = db.Column(db.Integer, nullable=False)
    current_hit_points = db.Column(db.Integer, nullable=False)
    hit_dice = db.Column(db.Text, nullable=False)
    strength = db.Column(db.Integer, nullable=False)
    dexterity = db.Column(db.Integer, nullable=False)
    constitution = db.Column(db.Integer, nullable=False)
    intelligence = db.Column(db.Integer, nullable=False)
    wisdom = db.Column(db.Integer, nullable=False)
    charisma = db.Column(db.Integer, nullable=False)
    strength_save = db.Column(db.Integer, nullable=True)
    dexterity_save = db.Column(db.Integer, nullable=True)
    constitution_save = db.Column(db.Integer, nullable=True)
    intelligence_save = db.Column(db.Integer, nullable=True)
    wisdom_save = db.Column(db.Integer, nullable=True)
    charisma_save = db.Column(db.Integer, nullable=True)
    perception = db.Column(db.Integer, nullable=True)
    damage_vulnerabilities = db.Column(db.ARRAY(db.Text), nullable=True)
    damage_resistances = db.Column(db.ARRAY(db.Text), nullable=True)
    damage_immunities = db.Column(db.ARRAY(db.Text), nullable=True)
    condition_immunities = db.Column(db.ARRAY(db.Text), nullable=True)
    languages = db.Column(db.ARRAY(db.Text), nullable=True)
    challenge_rating = db.Column(db.Integer, nullable=False)
    page_number = db.Column(db.Integer, nullable=True)
    document__slug = db.Column(db.Text, nullable=True)
    environments = db.Column(db.ARRAY(db.Text), nullable=True)
    img = db.Column(db.Text, nullable=True)
    concentration = db.Column(db.BOOLEAN, nullable=False)
    status_effects = db.Column(db.ARRAY(db.Text), nullable=False)
    senses = db.Column(db.ARRAY(db.Text), nullable=False)


class PlayerCharacter(db.Model):
    """"""

    __tablename__ = "player_characters"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class NonPlayerCharacter(db.Model):
    """"""

    __tablename__ = "nonplayer_characters"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class MonsterAction(db.Model):
    """"""

    __tablename__ = "monsters_actions"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    monster_id = db.Column(db.Integer, db.ForeignKey("monsters.id"))
    action_id = db.Column(db.Integer, db.ForeignKey("actions.id"))


class MonsterBonusAction(db.Model):
    """"""

    __tablename__ = "monsters_bonus_actions"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    monster_id = db.Column(db.Integer, db.ForeignKey("monsters.id"))
    action_id = db.Column(db.Integer, db.ForeignKey("actions.id"))


class MonsterReaction(db.Model):
    """"""

    __tablename__ = "monsters_reactions"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    monster_id = db.Column(db.Integer, db.ForeignKey("monsters.id"))
    action_id = db.Column(db.Integer, db.ForeignKey("actions.id"))


class MonsterLegendaryAction(db.Model):
    """"""

    __tablename__ = "monsters_legendary_actions"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    monster_id = db.Column(db.Integer, db.ForeignKey("monsters.id"))
    action_id = db.Column(db.Integer, db.ForeignKey("actions.id"))


class MonsterSpecialAbility(db.Model):
    """"""

    __tablename__ = "monsters_special_abilities"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    monster_id = db.Column(db.Integer, db.ForeignKey("monsters.id"))
    action_id = db.Column(db.Integer, db.ForeignKey("actions.id"))


class MonsterSpeed(db.Model):
    """"""

    __tablename__ = "monsters_speeds"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    monster_id = db.Column(db.Integer, db.ForeignKey("monsters.id"))
    speed_id = db.Column(db.Integer, db.ForeignKey("speeds.id"))


class MonsterSkills(db.Model):
    """"""

    __tablename__ = "monsters_skills"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    monster_id = db.Column(db.Integer, db.ForeignKey("monsters.id"))
    skills_id = db.Column(db.Integer, db.ForeignKey("skills.id"))


class MonsterSpell(db.Model):
    """"""

    __tablename__ = "monsters_spells"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    monster_id = db.Column(db.Integer, db.ForeignKey("monsters.id"))
    spell_id = db.Column(db.Integer, db.ForeignKey("spells.id"))


class PcAction(db.Model):
    """"""

    __tablename__ = "pcs_actions"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class PcBonusAction(db.Model):
    """"""

    __tablename__ = "pcs_bonus_actions"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class PcReaction(db.Model):
    """"""

    __tablename__ = "pcs_reactions"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class PcSpecialAbility(db.Model):
    """"""

    __tablename__ = "pcs_special_abilities"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class PcSpeed(db.Model):
    """"""

    __tablename__ = "pcs_speeds"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class PcSkills(db.Model):
    """"""

    __tablename__ = "pcs_skills"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class PcSpells(db.Model):
    """"""

    __tablename__ = "pcs_spells"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class NpcAction(db.Model):
    """"""

    __tablename__ = "npcs_actions"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class NpcBonusAction(db.Model):
    """"""

    __tablename__ = "npcs_bonus_actions"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class NpcReaction(db.Model):
    """"""

    __tablename__ = "npcs_reactions"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class NpcLegendaryAction(db.Model):
    """"""

    __tablename__ = "npcs_legendary_actions"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class NpcSpecialAbility(db.Model):
    """"""

    __tablename__ = "npcs_special_abilities"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class NpcSpeed(db.Model):
    """"""

    __tablename__ = "npcs_speeds"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class NpcSkills(db.Model):
    """"""

    __tablename__ = "npcs_skills"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class Action(db.Model):
    """"""

    __tablename__ = "actions"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    desc = db.Column(db.Text, nullable=True)
    attack_bonus = db.Column(db.Integer, nullable=True)
    damage_dice = db.Column(db.Text, nullable=True)
    damage_bonus = db.Column(db.Integer, nullable=True)
    action_type = db.Column(
        db.Text, nullable=False
    )  # Action, Bonus_Action, Reaction, Legendary_Action, Special
    recharge_type = db.Column(db.Text, nullable=True)  # X/Day, X-Y, Rest
    recharge_x = db.Column(db.Integer, nullable=True)
    hit_effect = db.Column(db.Text, nullable=True)
    miss_effect = db.Column(db.Text, nullable=True)


class Speed(db.Model):
    """"""

    __tablename__ = "speeds"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    speed_type = db.Column(db.Text, nullable=False)
    distance = db.Column(db.Integer, nullable=False)


class Skills(db.Model):
    """"""

    __tablename__ = "skills"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    athletics = db.Column(db.Integer, nullable=False)
    acrobatics = db.Column(db.Integer, nullable=False)
    sleight_of_hand = db.Column(db.Integer, nullable=False)
    stealth = db.Column(db.Integer, nullable=False)
    arcana = db.Column(db.Integer, nullable=False)
    history = db.Column(db.Integer, nullable=False)
    investigation = db.Column(db.Integer, nullable=False)
    nature = db.Column(db.Integer, nullable=False)
    religion = db.Column(db.Integer, nullable=False)
    animal_handling = db.Column(db.Integer, nullable=False)
    insight = db.Column(db.Integer, nullable=False)
    medicine = db.Column(db.Integer, nullable=False)
    perception = db.Column(db.Integer, nullable=False)
    survival = db.Column(db.Integer, nullable=False)
    deception = db.Column(db.Integer, nullable=False)
    intimidation = db.Column(db.Integer, nullable=False)
    performance = db.Column(db.Integer, nullable=False)
    persuasion = db.Column(db.Integer, nullable=False)


class Spell(db.Model):
    """"""

    __tablename__ = "spells"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    slug = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable=False)
    desc = db.Column(db.Text, nullable=True)
    higher_level = db.Column(db.Text, nullable=True)
    page = db.Column(db.Text, nullable=True)
    range = db.Column(db.Text, nullable=True)
    components = db.Column(db.Text, nullable=True)
    material = db.Column(db.Text, nullable=True)
    can_be_cast_as_ritual = db.Column(db.Boolean, nullable=True)
    duration = db.Column(db.Integer, nullable=True)
    requires_concentration = db.Column(db.Boolean, nullable=True)
    casting_time = db.Column(db.Integer, nullable=True)
    level = db.Column(db.Integer, nullable=True)
    spell_level = db.Column(db.Integer, nullable=True)
    school = db.Column(db.Text, nullable=False)


def connect_db(app):
    db.app = app
    db.init_app(app)
