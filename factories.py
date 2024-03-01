from api_handler import *
from models import Monster
from models import (
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


def skills_factory(skills: str):
    """Generates new Skills object

    Args:
        m (_type_): _description_
    """


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
        level=s["level"],
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


def add_new_monster(slug, extras):
    """
    Adds a new monster to the database.

    Args:
        slug (str): the unique name to pass to the api to get this monster
    """
    monster_json = get_instance("monsters", slug)  # get monster json from api
    # print(monster_json)
    if slug != monster_json["slug"]:
        return "error: monster slug is not valid"
    new_monster = monster_factory(monster_json)
    spells = parse_spells(monster_json)


add_new_monster("solar", 1)
