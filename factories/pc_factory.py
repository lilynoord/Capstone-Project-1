from models import (
    PlayerCharacter,
    PcSpeed,
    PcSkills,
    Speed,
    Skills,
)


def pc_factory(form):
    head = form.header_forms
    score = form.ability_forms
    save = form.saving_throws

    dmg = form.damage_forms
    mid = form.mid_forms
    pc = PlayerCharacter(
        player_name=head.player_name.data,
        name=head.character_name.data,
        size=head.size.data,
        creature_type=head.creature_type.data,
        alignment=head.alignment.data,
        armor_class=mid.armor_class.data,
        max_hit_points=mid.hit_point_maximum.data,
        hit_dice=str(mid.hit_dice_count.data) + "d" + str(mid.hit_dice_type.data),
        strength=score.strength.data,
        dexterity=score.dexterity.data,
        constitution=score.constitution.data,
        intelligence=score.intelligence.data,
        wisdom=score.wisdom.data,
        charisma=score.charisma.data,
        strength_save=save.strength.data,
        dexterity_save=save.dexterity.data,
        constitution_save=save.constitution.data,
        intelligence_save=save.intelligence.data,
        wisdom_save=save.wisdom.data,
        charisma_save=save.charisma.data,
        damage_vulnerabilities=dmg.damage_vulnerabilities.data,
        damage_resistances=dmg.damage_resistances.data,
        damage_immunities=dmg.damage_immunities.data,
        condition_immunities=dmg.condition_immunities.data,
        level=head.level.data,
        character_class=head.character_class.data,
    )
    print("NEW PC", pc.name, pc.id)
    return pc


def skills_factory(skill):
    """Generates new Skills object"""
    return Skills(
        athletics=skill.athletics.data,
        acrobatics=skill.athletics.data,
        sleight_of_hand=skill.athletics.data,
        stealth=skill.athletics.data,
        arcana=skill.athletics.data,
        history=skill.athletics.data,
        investigation=skill.athletics.data,
        nature=skill.athletics.data,
        religion=skill.athletics.data,
        animal_handling=skill.athletics.data,
        insight=skill.athletics.data,
        medicine=skill.athletics.data,
        perception=skill.athletics.data,
        survival=skill.athletics.data,
        deception=skill.athletics.data,
        intimidation=skill.athletics.data,
        performance=skill.athletics.data,
        persuasion=skill.athletics.data,
    )


def new_pc(form):
    pc = pc_factory(form)
    skills = skills_factory(form.skill_forms)

    speed = Speed(speed_type="default speed", distance=form.mid_forms.speed.data)

    print(pc.id)
    return [pc, skills, speed]
