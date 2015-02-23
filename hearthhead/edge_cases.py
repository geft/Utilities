__author__ = 'Gerry'


def rename_edge_cases(file_name):
    if " - Copy" in file_name:
        file_name = str.replace(file_name, " - Copy", "")

    if "NEW1_040" in file_name:
        file_name = str.replace(file_name, "Death_12", "Death")

    if "EX1_554t" in file_name:
        file_name = str.replace(file_name, "_Snake", "")
        file_name = str.replace(file_name, "_1", "1")
        file_name = str.replace(file_name, "_2", "2")

    if "EX1_614" in file_name:
        file_name = str.replace(file_name, "_15-01", "")

    if "EX1_623" in file_name:
        file_name = str.replace(file_name, "_1", "")
        file_name = str.replace(file_name, "_2", "")
        file_name = str.replace(file_name, "_4", "")

    if "GVG_011" in file_name:
        file_name = str.replace(file_name, "_Alt_03", "")

    if "NEW1_023" in file_name:
        file_name = str.replace(file_name, "_Faerie_Dragon", "")
        file_name = str.replace(file_name, "_2", "")
        file_name = str.replace(file_name, "_3", "")
        file_name = str.replace(file_name, "_2", "")

    if "HarrisonJ" in file_name:
        file_name = str.replace(file_name, "HarrisonJ_EX1_558_whip_attack", "EX1_558_Attack")

    if "Sylvanas" in file_name:
        card_id = "EX1_016"
        file_name = str.replace(file_name, "Sylvanas_01", card_id)
        file_name = str.replace(file_name, "Sylvanas_02", card_id)
        file_name = str.replace(file_name, "Sylvanas_04", card_id)

    if "Koto" in file_name or "Kodo" in file_name:
        file_name = str.replace(file_name, "KotoBeastReady1", "NEW1_041_Play")
        file_name = str.replace(file_name, "KotoBeastYes1", "NEW1_041_Attack")
        file_name = str.replace(file_name, "KodoBeastDeath", "NEW1_041_Death")

    return file_name