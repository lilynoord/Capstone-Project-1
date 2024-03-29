from __future__ import print_function
from tools import *
from flask import Flask, redirect, render_template, flash, request, make_response
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
    PcSpeed,
    PcSkills,
    NpcSpeed,
    NpcSkills,
    Action,
    Speed,
    Skills,
    Spell,
    TempMonster,
    TempNpc,
    TempPc,
    PcAction,
    NpcAction,
)
from api_handler import *
from factories.monster_factory import new_monster
from factories.pc_factory import new_pc
from factories.npc_factory import new_npc
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


def check_user(request):
    """Return true if the user is not logged in."""
    user = request.cookies.get("user_id", False)
    global current_user_key
    print(f"check_user - user: {user}, key:{current_user_key} ")
    if not user:
        return True
    current_user_key = user
    return False


@app.route("/")
def route_home():
    # if user is logged in, redir to users/games. If not, redir to login/signup
    print("Home")
    if current_user_key == "":
        return redirect("/login")
    else:
        return redirect(f"/games")


@app.route("/login", methods=["GET", "POST"])
def login():
    global current_user_key
    form = SignInForm()
    if form.is_submitted() and form.validate():
        if not form.new_account.data:
            user = User.query.where(User.name == form.name.data).first()
            print("login", form)
            if user:
                if user.password == form.password.data:
                    current_user_key = user.id
                else:
                    flash("Incorrect password", "error")
                    redirect("/login")
            else:
                flash("User not found", "error")
                redirect("/login")
        else:
            if not User.query.filter(User.name == form.name.data).first():
                newUser = User(name=form.name.data, password=form.password.data)
                db.session.add(newUser)
                db.session.commit()
                current_user_key = (
                    User.query.where(User.name == form.name.data).first().id
                )
            else:
                flash("Username already exists", "error")
                redirect("/login")
        html = redirect("/games")
        response = make_response(html)
        response.set_cookie("user_id", str(current_user_key))
        return response
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    global current_user_key
    current_user_key = ""
    return redirect("/")


@app.route("/games")
def games_list():
    if check_user(request):
        return redirect("/login")
    games = Game.query.where(Game.user_id == current_user_key)
    print("games: ", games)
    html = render_template("games.html", games=games)
    response = make_response(html)
    response.set_cookie("existing_slug", "False")
    response.set_cookie("existing_search", "False")
    return response


@app.route("/games/new-game", methods=["GET", "POST"])
def new_game():
    if check_user(request):
        return redirect("/login")
    form = NewGameForm()
    if form.is_submitted() and form.validate():
        newGame = Game(name=form.name.data, user_id=current_user_key)
        db.session.add(newGame)
        db.session.commit()
        return redirect(f"/games/{newGame.id}/add")
    return render_template("new-game.html", form=form)


@app.route("/games/<int:gameId>/delete-game")
def delete_game(gameId):
    # TODO: DELETE GAME AND EVERYTHING CONNECTED TO IT, EXCEPT FOR THE USER
    return redirect("/games")


@app.route("/games/<int:gameId>/add")
def add_entity_to_game(gameId):
    # TODO: list of options for adding things to the game
    if check_user(request):
        return redirect("/")
    game = Game.query.filter(Game.id == gameId).first_or_404()
    combats = Combat.query.filter(Combat.game_id == gameId).all()
    pcs_ids = GamePc.query.filter(GamePc.game_id == gameId).all()
    npcs_ids = GameNpc.query.filter(GameNpc.game_id == gameId).all()
    monsters_ids = GameMonster.query.filter(GameMonster.game_id == gameId).all()
    pcs = []
    npcs = []
    monsters = []

    for each in pcs_ids:
        pcs.append(
            PlayerCharacter.query.filter(PlayerCharacter.id == each.pc_id).first()
        )
    for each in npcs_ids:
        npcs.append(
            NonPlayerCharacter.query.filter(
                NonPlayerCharacter.id == each.npc_id
            ).first()
        )
    for each in monsters_ids:
        monsters.append(Monster.query.filter(Monster.id == each.monster_id).first())
    print(pcs, npcs, monsters)
    html = render_template(
        "add-to-game-options.html",
        gameId=gameId,
        game=game,
        combats=combats,
        pcs=pcs,
        npcs=npcs,
        monsters=monsters,
    )
    response = make_response(html)
    response.set_cookie("existing_slug", "False")
    response.set_cookie("existing_search", "False")
    global m_instance_store
    global m_search_store
    m_search_store = ""
    m_instance_store = ""
    return response


m_search_store = ""
m_instance_store = ""


@app.route("/games/<int:gameId>/add/creature", methods=["GET"])
def add_creature_to_game(gameId):
    if check_user(request):
        return redirect("/")
    # Logic for displaying the results
    global m_instance_store
    global m_search_store
    s_json = ""
    monster_data = request.cookies.get("m", "none")
    existing_search = bool(request.cookies.get("existing_search", False))
    existing_slug = bool(request.cookies.get("existing_slug", False))
    search = "none"
    game = Game.query.where(Game.id == gameId).first()
    print("Add Creature: ", game, game.name, game.id)
    search = request.args.get("search", "none")
    if request.args:
        if search != "none":

            results, results_names = get_monsters_by_name(request.args["search"])
            s_json = results
            m_search_store = s_json
            existing_search = True
        elif existing_search and m_search_store != "":
            s_json = m_search_store
        else:
            results, results_names = get_all_monsters()
            s_json = results["results"]
            m_search_store = s_json
            existing_search = True
        if request.args.get("slug", False):
            monster_data = get_instance("monsters", request.args["slug"])
            existing_slug = True
            m_instance_store = monster_data
            mods = get_saves(monster_data)
        elif existing_slug and m_instance_store != "":
            monster_data = m_instance_store
            mods = get_saves(monster_data)
        else:
            m = "none"
            existing_slug = False
            mods = 0
    else:
        html = redirect(f"/games/{gameId}/add/creature?search=none")
        response = make_response(html)
        response.set_cookie("existing_search", "False")
        response.set_cookie("existing_slug", "False")
        return response
    html = render_template(
        "new-monster.html",
        search=search,
        game=game,
        s_json=s_json,
        m=monster_data,
        mods=mods,
    )
    response = make_response(html)
    response.set_cookie("existing_search", str(existing_search))
    response.set_cookie("existing_slug", str(existing_slug))
    return response


@app.route("/games/<int:gameId>/add/creature", methods=["POST"])
def commit_creature_to_game(gameId):

    game = Game.query.filter(Game.id == gameId).first()
    slug = request.args.get("slug")
    if not slug:
        flash(f"Error adding monster slug: {slug}", "error")
    else:
        new_monster = create_new_monster(slug)
        new_game_monster = GameMonster(game_id=gameId, monster_id=new_monster.id)
        db.session.add(new_game_monster)
        db.session.commit()
        flash(f"{new_monster.name} added to {game.name}", "info")
    html = redirect(f"/games/{gameId}/add/creature")
    response = make_response(html)
    response.set_cookie("existing_slug", "False")
    response.set_cookie("existing_search", "False")
    global m_instance_store
    global m_search_store
    m_search_store = ""
    m_instance_store = ""
    return response


class_choices = [
    ("Barbarian", "Barbarian"),
    ("Bard", "Bard"),
    ("Cleric", "Cleric"),
    ("Druid", "Druid"),
    ("Fighter", "Fighter"),
    ("Monk", "Monk"),
    ("Paladin", "Paladin"),
    ("Ranger", "Ranger"),
    ("Rogue", "Rogue"),
    ("Sorcerer", "Sorcerer"),
    ("Warlock", "Warlock"),
    ("Wizard", "Wizard"),
    ("Artificer", "Artificer"),
    ("Blood Hunter", "Blood Hunter"),
]
alignment_choices = [
    ("Lawful Good"),
    ("Neutral Good"),
    ("Chaotic Good"),
    ("Lawful Neutral"),
    ("True Neutral"),
    ("Chaotic Neutral"),
    ("Lawful Evil"),
    ("Neutral Evil"),
    ("Chaotic Evil"),
]
size_choices = [
    ("Tiny"),
    ("Small"),
    ("Medium"),
    ("Large"),
    ("Huge"),
    ("Gargantuan"),
]
dmg_choices = [
    ("None"),
    ("Acid"),
    ("Bludgeoning"),
    ("Cold"),
    ("Fire"),
    ("Force"),
    ("Lightning"),
    ("Necrotic"),
    ("Piercing"),
    ("Poison"),
    ("Psychic"),
    ("Radiant"),
    ("Slashing"),
    ("Thunder"),
]
condition_choices = [
    ("None"),
    ("Blinded"),
    ("Charmed"),
    ("Deafened"),
    ("Exhaustion"),
    ("Frightened"),
    ("Grappled"),
    ("Incapacitated"),
    ("Invisible"),
    ("Paralyzed"),
    ("Petrified"),
    ("Poisoned"),
    ("Prone"),
    ("Restrained"),
    ("Stunned"),
    ("Unconscious"),
]


@app.route("/games/<int:gameId>/add/pc", methods=["GET", "POST"])
def add_pc_to_game(gameId):
    form = AddPcForm()
    form.header_forms.character_class.choices = class_choices
    form.header_forms.alignment.choices = alignment_choices
    form.header_forms.size.choices = size_choices

    form.damage_forms.damage_vulnerabilities.choices = dmg_choices
    form.damage_forms.damage_resistances.choices = dmg_choices
    form.damage_forms.damage_immunities.choices = dmg_choices
    form.damage_forms.condition_immunities.choices = condition_choices

    if form.is_submitted():
        obj_list = new_pc(form)
        pc = obj_list[0]
        skills = obj_list[1]
        speed = obj_list[2]

        db.session.add(speed)
        db.session.add(skills)
        db.session.add(pc)
        for each in obj_list[3]:
            db.session.add(each)
        db.session.commit()

        pc_skills = PcSkills(pc_id=pc.id, skills_id=skills.id)
        pc_speed = PcSpeed(pc_id=pc.id, speed_id=speed.id)
        db.session.add(pc_skills)
        db.session.add(pc_speed)
        game_pc = GamePc(game_id=int(gameId), pc_id=pc.id)
        db.session.add(game_pc)

        for each in obj_list[3]:
            pcAction = PcAction(pc_id=pc.id, action_id=each.id)
            db.session.add(pcAction)
        db.session.commit()

        flash(f"{pc.name} added to {Game.query.where(Game.id == gameId).first().name}")
        return redirect(f"/games/{gameId}/add")
    return render_template("add-pc.html", form=form)


@app.route("/games/<int:gameId>/add/npc", methods=["GET", "POST"])
def add_npc_to_game(gameId):
    form = AddPcForm()
    form.header_forms.character_class.choices = class_choices
    form.header_forms.alignment.choices = alignment_choices
    form.header_forms.size.choices = size_choices

    form.damage_forms.damage_vulnerabilities.choices = dmg_choices
    form.damage_forms.damage_resistances.choices = dmg_choices
    form.damage_forms.damage_immunities.choices = dmg_choices
    form.damage_forms.condition_immunities.choices = condition_choices

    if form.is_submitted():
        obj_list = new_npc(form)
        npc = obj_list[0]
        skills = obj_list[1]
        speed = obj_list[2]
        db.session.add(speed)
        db.session.add(skills)
        db.session.add(npc)
        for each in obj_list[3]:
            db.session.add(each)
        db.session.commit()
        npc_skills = NpcSkills(npc_id=npc.id, skills_id=skills.id)
        npc_speed = NpcSpeed(npc_id=npc.id, speed_id=speed.id)
        db.session.add(npc_skills)
        db.session.add(npc_speed)
        game_npc = GameNpc(game_id=int(gameId), npc_id=npc.id)
        db.session.add(game_npc)
        for each in obj_list[3]:
            npcAction = NpcAction(npc_id=npc.id, action_id=each.id)
            db.session.add(npcAction)
        db.session.commit()
        flash(f"{npc.name} added to {Game.query.where(Game.id == gameId).first().name}")
        return redirect(f"/games/{gameId}/add")
    return render_template("add-npc.html", form=form)


@app.route("/games/<int:gameId>/combat/new", methods=["GET", "POST"])
def combat_setup_new(gameId):
    form = NewCombatForm()
    if form.is_submitted() and form.validate():
        newCombat = Combat(name=form.name.data, game_id=gameId)
        db.session.add(newCombat)
        db.session.commit()
        return redirect(f"/games/{gameId}/combat/{newCombat.id}/setup")
    return render_template("new-combat.html", form=form)


@app.route("/games/<int:gameId>/combat/<int:combatId>/setup")
def combat_setup(gameId, combatId):
    game = Game.query.filter(Game.id == gameId).first_or_404()
    combat = Combat.query.filter(Combat.id == combatId).first_or_404()
    pcs_ids = GamePc.query.filter(GamePc.game_id == gameId).all()
    npcs_ids = GameNpc.query.filter(GameNpc.game_id == gameId).all()
    monsters_ids = GameMonster.query.filter(GameMonster.game_id == gameId).all()
    pcs = []
    npcs = []
    monsters = []

    for each in pcs_ids:
        pcs.append(
            PlayerCharacter.query.filter(PlayerCharacter.id == each.pc_id).first()
        )
    for each in npcs_ids:
        npcs.append(
            NonPlayerCharacter.query.filter(
                NonPlayerCharacter.id == each.npc_id
            ).first()
        )
    for each in monsters_ids:
        monsters.append(Monster.query.filter(Monster.id == each.monster_id).first())
    return render_template(
        "combat-setup.html",
        game=game,
        combat=combat,
        pcs=pcs,
        monsters=monsters,
        npcs=npcs,
    )


@app.route("/update-health", methods=["POST"])
def update_health():

    eType = request.json["eType"]
    print(eType)
    eId = int(request.json["eid"])
    if eType == "TempMonster":
        entity = TempMonster.query.filter(TempMonster.id == eId).first_or_404()
    elif eType == "TempPc":
        entity = TempPc.query.filter(TempPc.id == eId).first_or_404()
    elif eType == "TempNpc":
        entity = TempNpc.query.filter(TempNpc.id == eId).first_or_404()
    print(entity)
    entity.current_hit_points += request.json["value"]
    db.session.commit()
    return str(entity.current_hit_points)


def sortInitiative(val):
    return val.initiative


@app.route("/games/<int:gameId>/combat/<int:combatId>/play", methods=["GET"])
def combat_play(
    gameId,
    combatId,
):
    combat = Combat.query.filter(Combat.id == combatId).first_or_404()
    game = Game.query.filter(Game.id == gameId).first_or_404()
    entity_list = []

    # Get all the entities in the combat and put them in an unordered list
    for each in TempMonster.query.filter(TempMonster.combat_id == combatId):
        entity_list.append(each)
    for each in TempPc.query.filter(TempPc.combat_id == combatId):
        entity_list.append(each)
    for each in TempNpc.query.filter(TempNpc.combat_id == combatId):
        entity_list.append(each)
    print("ENTITIES", entity_list)

    # sort the entities by their initiative
    entity_list.sort(key=sortInitiative, reverse=True)
    entity_dict = {}

    # In the sorted order, give each entity its own unique initiative 'id'
    initiative_counter = 0
    for each in entity_list:
        each.initiative = initiative_counter
        initiative_counter += 1

    for each in entity_list:
        if type(each) == TempMonster:
            a = generate_monster_dict(each)
        elif type(each) == TempPc:
            actions = []
            for i in PcAction.query.filter(PcAction.pc_id == each.pc_id).all():
                actions.append(Action.query.filter(Action.id == i.action_id).first())
            a = {
                "temp": each,
                "verbose": PlayerCharacter.query.filter(
                    PlayerCharacter.id == each.pc_id
                ).first_or_404(),
                "actions": actions,
                "bonusActions": [],
                "reactions": [],
                "legendaryActions": [],
                "specials": [],
                "speeds": [],
                "spells": [],
                "skills": [],
            }
        elif type(each) == TempNpc:
            actions = []
            for i in NpcAction.query.filter(NpcAction.npc_id == each.npc_id).all():
                actions.append(Action.query.filter(Action.id == i.action_id).first())
            a = {
                "temp": each,
                "verbose": NonPlayerCharacter.query.filter(
                    NonPlayerCharacter.id == each.npc_id
                ).first_or_404(),
                "actions": actions,
                "bonusActions": [],
                "reactions": [],
                "legendaryActions": [],
                "specials": [],
                "speeds": [],
                "spells": [],
                "skills": [],
            }
        entity_dict[each.initiative] = a

    print("ENTITIES", entity_list)
    return render_template(
        "combat.html",
        game=game,
        combat=combat,
        entities=entity_dict,
        entity_count=initiative_counter,
    )


def generate_monster_dict(entity):
    verbose = Monster.query.filter(Monster.id == entity.monster_id).first_or_404()
    entityActions = MonsterAction.query.filter(
        MonsterAction.monster_id == verbose.id
    ).all()
    entityBonusActions = MonsterBonusAction.query.filter(
        MonsterBonusAction.monster_id == verbose.id
    ).all()
    entityReactions = MonsterReaction.query.filter(
        MonsterReaction.monster_id == verbose.id
    ).all()
    entityLegendary = MonsterLegendaryAction.query.filter(
        MonsterLegendaryAction.monster_id == verbose.id
    ).all()

    entitySpecials = MonsterSpecialAbility.query.filter(
        MonsterSpecialAbility.monster_id == verbose.id
    ).all()
    entitySpeeds = MonsterSpeed.query.filter(
        MonsterSpeed.monster_id == verbose.id
    ).all()
    entitySkills = MonsterSkills.query.filter(
        MonsterSkills.monster_id == verbose.id
    ).all()
    entitySpells = MonsterSpell.query.filter(
        MonsterSpell.monster_id == verbose.id
    ).all()

    actions = []
    bonusActions = []
    reactions = []
    legendaryActions = []
    specials = []
    speeds = []
    skills = []
    spells = []

    for each in entityActions:
        actions.append(Action.query.filter(Action.id == each.action_id).first())
    for each in entityBonusActions:
        bonusActions.append(Action.query.filter(Action.id == each.action_id).first())
    for each in entityReactions:
        reactions.append(Action.query.filter(Action.id == each.action_id).first())
    for each in entityLegendary:
        legendaryActions.append(
            Action.query.filter(Action.id == each.action_id).first()
        )
    for each in entitySpecials:
        specials.append(Action.query.filter(Action.id == each.action_id).first())

    for each in entitySpeeds:
        speeds.append(Speed.query.filter(Speed.id == each.speed_id).first())
    for each in entitySkills:
        skills.append(Skills.query.filter(Skills.id == each.skills_id).first())
    for each in entitySpells:
        spells.append(Spell.query.filter(Spell.id == each.spell_id).first())
    return {
        "temp": entity,
        "verbose": verbose,
        "actions": actions,
        "bonusActions": bonusActions,
        "reactions": reactions,
        "legendaryActions": legendaryActions,
        "specials": specials,
        "speeds": speeds,
        "spells": spells,
        "skills": skills,
    }


""" Entity Dict Format:
    entity_dict = {
        initiative: {
            'temp': TempMonster | TempPc | TempNpc,
            'verbose': Monster | PlayerCharacter | NonPlayerCharacter,
            'actions': [Action],
            'bonusActions': [Action],
            'reactions': [Action],
            'legendaryActions': [Action],
            'specials':[Action],
            'speeds':[Speed],
            'spells': [Spells],
            'skills': [Skills]
        }
    }
    
    
    """


@app.route("/games/combat/submit-combat/<int:combatId>", methods=["POST"])
def submit_combat(combatId):
    print("REQUEST:", request.json)
    entity_list = request.json["entity_list"]
    print("ENTITY_LIST", entity_list)
    combat = Combat.query.filter(Combat.id == combatId).first_or_404()
    initiative_counter = 0
    for each in entity_list:
        if each != "REMOVED":
            if each["kind"] == "monster":
                entity = Monster.query.filter(
                    Monster.id == int(each["id"])
                ).first_or_404()
                temp_entity = TempMonster(
                    combat_id=combatId,
                    monster_id=entity.id,
                    max_hit_points=entity.max_hit_points,
                    current_hit_points=entity.max_hit_points,
                    concentration=False,
                    status_effects=[],
                    initiative=each["initiative"],
                )
                db.session.add(temp_entity)
            elif each["kind"] == "pc":
                entity = PlayerCharacter.query.filter(
                    PlayerCharacter.id == int(each["id"])
                ).first_or_404()
                temp_entity = TempPc(
                    combat_id=combatId,
                    pc_id=entity.id,
                    max_hit_points=entity.max_hit_points,
                    current_hit_points=entity.max_hit_points,
                    concentration=False,
                    status_effects=[],
                    initiative=each["initiative"],
                )
                db.session.add(temp_entity)
            elif each["kind"] == "npc":
                entity = NonPlayerCharacter.query.filter(
                    NonPlayerCharacter.id == int(each["id"])
                ).first_or_404()
                temp_entity = TempNpc(
                    combat_id=combatId,
                    npc_id=entity.id,
                    max_hit_points=entity.max_hit_points,
                    current_hit_points=entity.max_hit_points,
                    concentration=False,
                    status_effects=[],
                    initiative=each["initiative"],
                )
                db.session.add(temp_entity)
    db.session.commit()
    print(entity_list)
    return "True"


def create_new_monster(slug):
    """
    Adds a new monster to the database. Don't forget to add a new games_monsters entry as well.

    Args:
        slug (str): the unique name to pass to the api to get this monster
    """

    new_mon, db_entries = new_monster(session=db.session, slug=slug)
    print("Create_New_Monster: ", db_entries)

    # Go through the list of new db entries and add them to the session.
    for each in db_entries:
        for entry in db_entries[each]:
            db.session.add(entry)
    db.session.commit()
    return new_mon
