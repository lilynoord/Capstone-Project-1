from __future__ import print_function
import sys

from flask import Flask, redirect, render_template, flash
from sqlalchemy import select
from models import (
    db,
    connect_db,
    User,
    Game,
    GameMonster,
    GamePc,
    GameNpc,
    Combat,
    CombatMonster,
    CombatPc,
    CombatNpc,
    Monster,
    PlayerCharacter,
    NonPlayerCharacter,
    MonsterAction,
    MonsterBonusAction,
    MonsterReaction,
    MonsterLegendaryAction,
    MonsterSpecialAbility,
    MonsterSpeed,
    MonsterSkills,
    MonsterSpell,
    PcAction,
    PcBonusAction,
    PcReaction,
    PcSpecialAbility,
    PcSpeed,
    PcSkills,
    PcSpells,
    NpcAction,
    NpcBonusAction,
    NpcReaction,
    NpcLegendaryAction,
    NpcSpecialAbility,
    NpcSpeed,
    NpcSkills,
    Action,
    Speed,
    Skills,
    Spell,
)
from api_handler import *

app = Flask(__name__)

app.app_context().push()
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///dnd-utils"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

connect_db(app)

current_user_key = ""
with app.app_context():
    db.create_all()

app.config["SECRET_KEY"] = "I Have A Secret!"


@app.route("/")
def route_home():
    # if user is logged in, redir to users/games. If not, redir to login/signup
    if current_user_key == "":
        return redirect("/login")
    else:
        return redirect(f"/games")


@app.route("/login", methods=["GET", "POST"])
def login():
    # TODO: form to login or signup
    form = None
    if form.is_submitted() and form.validate():

        return redirect("/games")
    return render_template("login.html")


@app.route("/logout")
def logout():
    global current_user_key
    current_user_key = ""
    return redirect("/")


@app.route("/users/<uuid>/games")
def games_list(uuid):
    # TODO: get list of the users games
    return render_template("games.html")


@app.route("/users/<uuid>/new-game")
def new_game(uuid):
    # TODO: Form to add a new game
    return render_template("new-game.html")


@app.route("/users/<uuid>/games/<gameId>")
def game_details(uuid, gameId):
    # TODO: Get list of game's active combats and players, plus options to add to the game or start new combat
    return render_template("game-details.html")


@app.route("/users/<uuid>/games/<gameId>/add")
def add_entity_to_game(uuid, gameId):
    # TODO: list of options for adding things to the game
    return render_template("add-to-game-options.html")


@app.route("/games/<gameId>/add/creature")
def add_creature_to_game(gameId):
    # TODO: Add creature form
    return render_template("")


@app.route("/games/<gameId>/add/pc")
def add_pc_to_game(gameId):
    # TODO: add pc form
    return render_template("")


@app.route("/games/<gameId>/add/npc")
def add_npc_to_game(gameId):
    # TODO: Add npc form
    return render_template("")


@app.route("/games/<gameId>/combat/<combatId>")
def combat_master(gameId, combatId):
    # TODO: option to either setup combat or start combat
    return render_template("")


@app.route("/games/<gameId>/combat/<combatId>/setup/new")
def combat_setup_new(gameId, combatId):
    return render_template("")


@app.route("/games/<gameId>/combat/<combatId>/setup/add-pcs")
def combat_setup_pcs(gameId, combatId):
    return render_template("")


@app.route("/games/<gameId>/combat/<combatId>/setup/add-npcs")
def combat_setup_npcs(gameId, combatId):
    return render_template("")


@app.route("/games/<gameId>/combat/<combatId>/setup/add-creatures")
def combat_setup_creatures(gameId, combatId):
    return render_template("")


@app.route("/games/<gameId>/combat/<combatId>/setup/confirm")
def combat_setup_confirm(gameId, combatId):
    return render_template("")


@app.route("/games/<gameId>/combat/<combatId>/play/set-initiative")
def combat_set_initiative(gameId, combatId):
    return render_template("")


@app.route("/games/<gameId>/combat/<combatId>/play/<turn>")
def combat_play(gameId, combatId, turn):
    return render_template("")


@app.route("/games/<gameId>/<pcId>")
def view_pc(pcId):
    return render_template("")


@app.route("/games/<gameId>/<npcId>")
def view_npc(npcId):
    return render_template("")


# TODO: Move this to own file?
def add_new_monster(slug, extras):
    """_summary_

    Args:
        slug (str): the unique name to pass to the api to get this monster
    """
    monster = get_instance("monsters", slug)  # get monster json from api
    m = monster  # monster for readability, m for my own sanity.
    if slug != monster.slug:
        return "error: monster slug is not valid"

    newMonster = Monster(
        name=m.name,
        size=m.size,
        type=m.type,
        alignment=m.alignment,
        armor_class=m.armor_class,
        armor_desc=m.armor_desc,
        max_hit_points=m.hit_points,
        current_hit_points=m.hit_points,
        hit_dice=m.hit_dice,
        strength=m.strength,
        dexterity=m.dexterity,
        constitution=m.constitution,
        intelligence=m.intelligence,
        wisdom=m.wisdom,
        charisma=m.charisma,
        strength_save=m.strength_save,
        dexterity_save=m.dexterity_save,
        constitution_save=m.constitution_save,
        intelligence_save=m.intelligence_save,
        wisdom_save=m.wisdom_save,
        charisma_save=m.charisma_save,
        perception=m.perception,
        damage_vulnerabilities=m.damage_vulnerabilities.split(", "),
        damage_resistances=m.damage_resistances.split(", "),
        damage_immunities=m.damage_immunities.split(", "),
        condition_immunities=m.condition_immunities.split(", "),
    )
