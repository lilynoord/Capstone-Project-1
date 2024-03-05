from __future__ import print_function
import sys

from flask import Flask, redirect, render_template, flash, request
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
from factories.monster_factory import new_monster
from forms import *

app = Flask(__name__)

app.app_context().push()
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///dnd-utils"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config["SQLALCHEMY_ECHO"] = True

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
    global current_user_key
    form = SignInForm()
    if form.is_submitted() and form.validate():
        user = User.query.where(User.name == form.name.data).first()
        if user:
            current_user_key = user.id
        else:
            newUser = User(name=form.name.data)
            db.session.add(newUser)
            db.session.commit()
            current_user_key = User.query.where(User.name == form.name.data).first().id
        return redirect("/games")
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    global current_user_key
    current_user_key = ""
    return redirect("/")


@app.route("/games")
def games_list():

    return render_template("games.html")


@app.route("/games/new-game", methods=["GET", "POST"])
def new_game():
    global current_user_key
    if current_user_key == "":
        return redirect("/")
    form = NewGameForm()
    if form.is_submitted() and form.validate():
        newGame = Game(name=form.name.data, user_id=current_user_key)
        db.session.add(newGame)
        db.session.commit()
        return redirect(f"/games/{newGame.id}/add")
    return render_template("new-game.html", form=form)


@app.route("/games/<gameId>")
def game_details(uuid, gameId):
    # TODO: Get list of game's active combats and players, plus options to add to the game or start new combat
    return render_template("game-details.html")


@app.route("/games/<gameId>/add")
def add_entity_to_game(gameId):
    # TODO: list of options for adding things to the game
    return render_template("add-to-game-options.html", gameId=gameId)


m_search_store = ""
m_instance_store = ""


@app.route("/games/<gameId>/add/creature", methods=["GET", "POST"])
def add_creature_to_game(gameId):

    # Logic for displaying the results
    global m_instance_store
    global m_search_store
    s_json = ""
    monster_data = ""
    existing_search = False
    existing_slug = False
    search = "none"
    if request.args:
        if request.args.get("existing-search"):
            s_json = m_search_store
            existing_search = True
        else:
            search = request.args["search"]
            if search != "none":
                results, results_names = get_monsters_by_name(request.args["search"])
                s_json = results["results"]
                m_search_store = s_json
                existing_search = True
            else:

                results, results_names = get_all_monsters()
                s_json = results["results"]
                m_search_store = s_json
                existing_search = True
        if request.args.get("slug"):
            if request.args.get("existing-slug"):
                existing_slug = True
                monster_data = m_instance_store
            else:
                monster_data = get_instance("monsters", request.args["slug"])
                existing_slug = True
                m_instance_store = monster_data
    else:
        return redirect(f"/games/{gameId}/add/creature?search=none")
    return render_template(
        "new-monster.html",
        search=search,
        gameId=gameId,
        s_json=s_json,
        m=monster_data,
        existing_search=existing_search,
        existing_slug=existing_slug,
    )


@app.route("/games/<gameId>/add/creature/custom")
def add_custom_creature_to_game(gameId):
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


@app.route("/games/<gameId>/list_monsters")
def list_monsters(gameId):
    return render_template("gameMonsters")


@app.route("/games/<gameId>/list_monsters/<monsterId>")
def view_monster(monsterId):
    return render_template("viewMonster.html")


@app.route("/games/<gameId>/<npcId>")
def view_npc(npcId):
    return render_template("")


def create_new_monster(slug):
    """
    Adds a new monster to the database. Don't forget to add a new games_monsters entry as well.

    Args:
        slug (str): the unique name to pass to the api to get this monster
    """

    db_entries = new_monster(slug)
    print(db_entries)

    # Go through the list of new db entries and add them to the session.
    for each in db_entries:
        print(each)
        for entry in db_entries[each]:
            db.session.add(entry)
    db.session.commit()
    return db_entries["creature"][0]
