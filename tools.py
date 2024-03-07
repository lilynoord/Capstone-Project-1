import math


def calculate_modifier(score, save=None):
    mod = 0
    if save:
        mod = math.floor((save - 10) / 2)

    else:
        mod = math.floor((score - 10) / 2)

    if mod < 0:
        return str(mod)
    else:
        return "+" + str(mod) + ","


def get_saves(m="none"):
    if m != "none":
        mods = {
            "saves": {
                "Str": calculate_modifier(
                    m["strength"],
                    m["strength_save"],
                ),
                "Dex": calculate_modifier(
                    m["dexterity"],
                    m["dexterity_save"],
                ),
                "Con": calculate_modifier(
                    m["constitution"],
                    m["constitution_save"],
                ),
                "Int": calculate_modifier(
                    m["intelligence"],
                    m["intelligence_save"],
                ),
                "Wis": calculate_modifier(
                    m["wisdom"],
                    m["wisdom_save"],
                ),
                "Cha": calculate_modifier(
                    m["charisma"],
                    m["charisma_save"],
                ),
            },
            "skills": {},
        }
        for each in m["skills"]:

            mods["skills"][each] = calculate_modifier(m["skills"][each], None)

        return mods
    return None
