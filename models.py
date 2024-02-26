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


class MonsterBonusAction(db.Model):
    """"""

    __tablename__ = "monsters_bonus_actions"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class MonsterReaction(db.Model):
    """"""

    __tablename__ = "monsters_reactions"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class MonsterLegendaryAction(db.Model):
    """"""

    __tablename__ = "monsters_legendary_actions"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class MonsterSpecialAbility(db.Model):
    """"""

    __tablename__ = "monsters_special_abilities"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class MonsterSpeed(db.Model):
    """"""

    __tablename__ = "monsters_speeds"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class MonsterSkills(db.Model):
    """"""

    __tablename__ = "monsters_skills"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class MonsterSpell(db.Model):
    """"""

    __tablename__ = "monsters_spells"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


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


class Speed(db.Model):
    """"""

    __tablename__ = "speeds"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class Skills(db.Model):
    """"""

    __tablename__ = "skills"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class Spell(db.Model):
    """"""

    __tablename__ = "spells"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


def connect_db(app):
    db.app = app
    db.init_app(app)
