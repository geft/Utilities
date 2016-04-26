__author__ = 'Gerry'


def remove_keyword(file_name, keyword):
    if keyword in file_name:
        file_name = str.replace(file_name, keyword, "")

    return file_name


def remove_keyword_and_1(file_name, keyword):
    if keyword in file_name:
        file_name = str.replace(file_name, "_1.", ".")
        file_name = str.replace(file_name, keyword, "")

    return file_name


def remove_keyword_on_condition(file_name, condition, keyword):
    if condition in file_name:
        file_name = str.replace(file_name, keyword, "")

    return file_name


def rename_edge_cases(file_name):
    file_name = remove_keyword_on_condition(file_name, "NEW1_040", "_12")
    file_name = remove_keyword_on_condition(file_name, "_Snake", "_1")
    file_name = remove_keyword_on_condition(file_name, "_Snake", "_2")
    file_name = remove_keyword(file_name, "_Snake")
    file_name = remove_keyword_on_condition(file_name, "EX1_614", "_15-01")
    file_name = remove_keyword_on_condition(file_name, "EX1_623", "_1")
    file_name = remove_keyword_on_condition(file_name, "EX1_623", "_2")
    file_name = remove_keyword_on_condition(file_name, "EX1_623", "_4")
    file_name = remove_keyword_on_condition(file_name, "_Faerie_Dragon", "_2")
    file_name = remove_keyword_on_condition(file_name, "_Faerie_Dragon", "_3")
    file_name = remove_keyword_and_1(file_name, "_Faerie_Dragon")
    file_name = remove_keyword_and_1(file_name, "VolcanicLumberer_")
    file_name = remove_keyword_and_1(file_name, "FirecatForm_")
    file_name = remove_keyword_and_1(file_name, "FirehawkForm_")
    file_name = remove_keyword_and_1(file_name, "CoreRager_")
    file_name = remove_keyword_and_1(file_name, "DragonConsort_")
    file_name = remove_keyword_and_1(file_name, "4 DragonEgg_")
    file_name = remove_keyword_and_1(file_name, "VolcanicDrake_")
    file_name = remove_keyword_and_1(file_name, "HungryDragon_")
    file_name = remove_keyword_and_1(file_name, "MajordomoExecutus_")
    file_name = remove_keyword_and_1(file_name, "Chromaggus_")
    file_name = remove_keyword_and_1(file_name, "HungryDragon_")
    file_name = remove_keyword_on_condition(file_name, "BRM_028", "_08")
    file_name = remove_keyword_on_condition(file_name, "BRM_029", "_10")
    file_name = remove_keyword_on_condition(file_name, "BRM_030", "_20")
    file_name = remove_keyword_on_condition(file_name, "BRM_030", "_21")
    file_name = remove_keyword(file_name, "_Lightwell - Copy")
    file_name = remove_keyword(file_name, "_Lightwell")
    file_name = remove_keyword_on_condition(file_name, "EX1_158t", " Treant")
    file_name = remove_keyword_on_condition(file_name, "EX1_573t", " Treant")
    file_name = remove_keyword_on_condition(file_name, "EX1_531", "_1")
    file_name = remove_keyword_on_condition(file_name, "AT_036", "_Alternate1_08")
    file_name = remove_keyword_on_condition(file_name, "AT_036", "1_05")
    file_name = remove_keyword_on_condition(file_name, "AT_081", "1_02")
    file_name = remove_keyword_on_condition(file_name, "AT_087", "1_02")
    file_name = remove_keyword_on_condition(file_name, "AT_093", "1_04")
    file_name = remove_keyword_on_condition(file_name, "AT_098", "1_02")
    file_name = remove_keyword_on_condition(file_name, "AT_100", "1_04")
    file_name = remove_keyword_on_condition(file_name, "AT_110", "1_04")
    file_name = remove_keyword_on_condition(file_name, "AT_111", "1_02")
    file_name = remove_keyword_on_condition(file_name, "AT_114", "1_02")
    file_name = remove_keyword_on_condition(file_name, "AT_124", "2_03")
    file_name = remove_keyword_on_condition(file_name, "AT_131", "1_02")
    file_name = remove_keyword_on_condition(file_name, "AT_133", "1_03")

    if "Sylvanas" in file_name:
        file_name = str.replace(file_name, "Sylvanas", "EX1_016")
        file_name = remove_keyword(file_name, "_01")
        file_name = remove_keyword(file_name, "_02")
        file_name = remove_keyword(file_name, "_04")

    if "HexFrog" in file_name:
        file_name = str.replace(file_name, "HexFrog", "hexfrog")

    if "Gnoll" in file_name:
        file_name = str.replace(file_name, "GnollReady1", "NEW1_040t_Ready")
        file_name = str.replace(file_name, "GnollPissed2", "NEW1_040t_Pissed")

    if "EX1_558_whip_attack" in file_name:
        file_name = str.replace(file_name, "HarrisonJ_EX1_558_whip_attack", "EX1_558_Attack")

    if "Koto" in file_name or "Kodo" in file_name:
        file_name = str.replace(file_name, "KotoBeastReady1", "NEW1_041_Play")
        file_name = str.replace(file_name, "KotoBeastYes1", "NEW1_041_Attack")
        file_name = str.replace(file_name, "KodoBeastDeath", "NEW1_041_Death")

    if "Jaraxxus" in file_name or "Jaxus" in file_name:
        file_name = str.replace(file_name, "Jaraxxus_Spin_Whoosh_01", "CS2_064_Spin")
        file_name = str.replace(file_name, "Jaraxxus_Start_Whoosh_01", "CS2_064_Start")
        file_name = str.replace(file_name, "Jaxus", "CS2_064_Summon")

    if "whirlwindshort" in file_name:
        file_name = str.replace(file_name, "whirlwindshort", "EX1_400_Play")

    if "spell_wr_innerrage_impact_01" in file_name:
        file_name = str.replace(file_name, "spell_wr_innerrage_impact_01", "EX1_607e_Effect")

    if "CS2_197" in file_name:
        file_name = str.replace(file_name, "MIX", "Mix")

    if "Stinger" in file_name:
        file_name = str.replace(file_name, "Beast_Play_Stinger_2", "Stinger_Beast")
        file_name = str.replace(file_name, "Battle_Play_Stinger_3", "Stinger_Battle_01")
        file_name = str.replace(file_name, "Battle_Play_Stinger_4", "Stinger_Battle_02")
        file_name = str.replace(file_name, "Alliance_Play_Stinger_2", "Stinger_Alliance")
        file_name = str.replace(file_name, "Blingtron_Play_Stinger", "GVG_119_Stinger")
        file_name = str.replace(file_name, "MalGanis_Play_Stinger", "GVG_021_Stinger")
        file_name = str.replace(file_name, "PlayCardStinger_Harrison_Jones", "EX1_558_Stinger")
        file_name = str.replace(file_name, "Pegasus_Stinger_Twisting_Nether", "EX1_312_Stinger")
        file_name = str.replace(file_name, "Pegasus_Stinger_Deathwing3", "NEW1_030_Stinger")
        file_name = str.replace(file_name, "Pegasus_Stinger_Leeroy_Jenkins", "EX1_116_Stinger")
        file_name = str.replace(file_name, "Pegasus_Stinger_Ragnaros", "EX1_298_Stinger")
        file_name = str.replace(file_name, "Gnome_Play_Stinger_2", "Stinger_Gnome")
        file_name = str.replace(file_name, "Goblin_Play_Stinger_1", "Stinger_Goblin")
        file_name = str.replace(file_name, "Neptulon_Play_Stinger", "GVG_042_Stinger")
        file_name = str.replace(file_name, "Hyjal_Play_Stinger_1", "Stinger_Hyjal")
        file_name = str.replace(file_name, "GarroshTheme_Play_Stinger_1", "Stinger_Garrosh")
        file_name = str.replace(file_name, "Ulduar_Play_Stinger_1", "Stinger_Ulduar")
        file_name = str.replace(file_name, "Troll_Play_Stinger_1", "Stinger_Troll")
        file_name = str.replace(file_name, "ETC_Play_Stinger_Horde", "PRO_001_Horde")
        file_name = str.replace(file_name, "ETC_Play_Stinger_Murloc", "PRO_001_Murloc")
        file_name = str.replace(file_name, "Pegasus_Stinger_Horde2", "Stinger_Horde")
        file_name = str.replace(file_name, "Pegasus_Stinger_Undead1", "Stinger_Undead")
        file_name = str.replace(file_name, "Pegasus_Stinger_War", "Stinger_War")
        file_name = str.replace(file_name, "Pegasus_Stinger_Lesser_Villain", "Stinger_Villain")

    if "AT_027_JARAXXUS" in file_name:
        file_name = str.replace(file_name, "AT_027_JARAXXUS", "AT_027_Jaraxxus")

    if "PLAY" in file_name:
        file_name = str.replace(file_name, "PLAY", "Play")
    elif "ATTACK" in file_name:
        file_name = str.replace(file_name, "ATTACK", "Attack")
    elif "DEATH" in file_name:
        file_name = str.replace(file_name, "DEATH", "Death")
    elif "TRIGGER" in file_name:
        file_name = str.replace(file_name, "TRIGGER", "Trigger")

    return file_name
