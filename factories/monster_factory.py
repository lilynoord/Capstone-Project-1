from api_handler import get_instance
import requests
from models import (
    db,
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

# TODO: Move this to own file?


def monster_factory(m):
    """
    Returns a new `Monster` object

    Args:
        m (dict): json returned by api

    Returns:
        `Monster`: new `Monster` object generated using the api json.
    """
    return Monster(
        slug=m["slug"],
        name=m["name"],
        size=m["size"],
        creature_type=m["type"],
        alignment=m["alignment"],
        armor_class=m["armor_class"],
        armor_desc=m["armor_desc"],
        max_hit_points=m["hit_points"],
        hit_dice=m["hit_dice"],
        strength=m["strength"],
        dexterity=m["dexterity"],
        constitution=m["constitution"],
        intelligence=m["intelligence"],
        wisdom=m["wisdom"],
        charisma=m["charisma"],
        strength_save=m["strength_save"],
        dexterity_save=m["dexterity_save"],
        constitution_save=m["constitution_save"],
        intelligence_save=m["intelligence_save"],
        wisdom_save=m["wisdom_save"],
        charisma_save=m["charisma_save"],
        perception=m["perception"],
        damage_vulnerabilities=m["damage_vulnerabilities"].split(", "),
        damage_resistances=m["damage_resistances"].split(", "),
        damage_immunities=m["damage_immunities"].split(", "),
        condition_immunities=m["condition_immunities"].split(", "),
        senses=senses_parser(m["senses"]),
        languages=m["languages"].split(", "),
        challenge_rating=m["cr"],
        page_number=m["page_no"],
        environments=m["environments"],
        img=m["img_main"],
        document__slug=m["document__slug"],
    )


def senses_parser(senses):
    """
    Takes the string of the creature's senses returned by the api and parses it into a dictionary.

    Args:
        senses (`str`): senses json string

    Returns:
        `dict`: a dictionary of the senses with the format of `'Sense':'Distance (ft)'`
    """
    split_senses = senses.split(" ft., ")
    senses_dict = {}
    for each in split_senses:
        sep = each.split(" ")
        if sep[0] == "passive":
            senses_dict["passive Perception"] = sep[2]
        else:
            senses_dict[sep[0]] = sep[1]
    return senses_dict


def action_factory(action: str):
    """
    Generates new Action object.
    """


def speed_factory(speed: str):
    """Generates new Speed object

    Args:
        m (_type_): _description_
    """


def skills_factory(skills: dict[str, int]):
    """Generates new Skills object"""
    return Skills(
        athletics=skills.setdefault("athletics", None),
        acrobatics=skills.setdefault("acrobatics", None),
        sleight_of_hand=skills.setdefault("sleight_of_hand", None),
        stealth=skills.setdefault("stealth", None),
        arcana=skills.setdefault("arcana", None),
        history=skills.setdefault("history", None),
        investigation=skills.setdefault("investigation", None),
        nature=skills.setdefault("nature", None),
        religion=skills.setdefault("religion", None),
        animal_handling=skills.setdefault("animal_handling", None),
        insight=skills.setdefault("insight", None),
        medicine=skills.setdefault("medicine", None),
        perception=skills.setdefault("perception", None),
        survival=skills.setdefault("survival", None),
        deception=skills.setdefault("deception", None),
        intimidation=skills.setdefault("intimidation", None),
        performance=skills.setdefault("performance", None),
        persuasion=skills.setdefault("persuasion", None),
    )


def spell_factory(url):
    """Generates a new Spell object

    Args:
        url (str): _spell url_
    """
    s = requests.get(url).json()
    return Spell(
        slug=s["slug"],
        name=s["name"],
        desc=s["desc"],
        higher_level=s["higher_level"],
        page=s["page"],
        range=s["range"],
        components=s["components"],
        material=s["material"],
        can_be_cast_as_ritual=s["can_be_cast_as_ritual"],
        duration=parse_spell_duration(s["duration"]),
        requires_concentration=s["requires_concentration"],
        casting_time=s["casting_time"],
        level=s["level_int"],
        spell_level=s["spell_level"],
        school=s["school"],
    )


def parse_spell_duration(duration):
    """
    parses a plaintext duration into a number of seconds. Returns an int.
    """
    if duration == "Instantaneous":
        return 0
    else:
        dsplit = duration.split(" ")
        if dsplit[1] == "minute" or dsplit[1] == "minutes":
            return int(dsplit[0]) * 60
        elif dsplit[1] == "hour" or dsplit[1] == "hours":
            return int(dsplit[0]) * 3600
        else:
            return 6


def parse_spells(m):
    """Loops over spells, generating new spell objects and returning a list of those objects.

    Args:
        m (_type_): _description_
    """
    spells = []

    for each in m["spell_list"]:
        spells.append(spell_factory(each))
    return spells


def parse_actions(m):
    actions = []
    bonus_actions = []
    reactions = []
    legendary_actions = []
    special_abilities = []
    for action in m["actions"]:
        actions.append(action_factory)

    return {
        "actions": actions,
        "bonus_actions": bonus_actions,
        "reactions": reactions,
        "legendary_actions": legendary_actions,
        "special_abilities": special_abilities,
    }


def parse_speeds(m):
    speeds = []
    for speed in m["speed"]:
        speeds.append(Speed(speed_type=speed, distance=m["speed"][speed]))
    return speeds


def parse_skills(m):
    skills = skills_factory(m["skills"])
    return skills


def new_monster(slug="", custom_monster=False, custom_monster_data=dict[str, str]):
    """
    Handles everything involved with adding a new monster to a game, except for adding it to the database. Returns a dictionary of lists of objects, all of which should be added to the database in app.py

    Args:
        slug (str, optional): api slug. Defaults to "".
        custom_monster (bool, optional): whether or not you are adding a custom monster. Defaults to False.
        custom_monster_data (dict[str, str], optional): If adding a custom monster, the data for said monster. Defaults to {}.

    Returns:
        db_entries (dict[str, list]) : A dictionary of lists of objects, to be added to the database by the calling function.
    """
    db_entries = {
        "creature": [],
        "spells": [],
        "actions": [],
        "skills": [],
        "speeds": [],
    }

    # If it's not a custom monster, then it should call the api and create a new set of entries for the database from that.
    if not custom_monster:
        # get monster json from api
        monster_json = get_instance("monsters", slug)
        if slug != monster_json["slug"]:  # Check to make sure api call was successful
            return "error: monster slug is not valid"

        new_monster = monster_factory(monster_json)
        db_entries["creature"] = [new_monster]
        spells = parse_spells(monster_json)
        actions = parse_actions(monster_json)
        speeds = parse_speeds(monster_json)
        skills = parse_skills(monster_json)

        # Add each object to db_entries, as well as a new relational object for each.
        for each in spells:
            db_entries["spells"].append(each)
            mtm = MonsterSpell(monster_id=new_monster.id, spell_id=each.id)
            db_entries["spells"].append(mtm)

        for each in speeds:
            db_entries["speeds"].append(each)
            mtm = MonsterSpeed(monster_id=new_monster.id, speed_id=each.id)
            db_entries["speeds"].append(mtm)

        db_entries["skills"].append(skills)
        db_entries["skills"].append(
            MonsterSkills(monster_id=new_monster.id, skills_id=each.id)
        )
        return db_entries
