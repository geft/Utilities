from hearthhead.edge_cases import rename_edge_cases

__author__ = 'Gerry'


def reformat_sound_name(file_name):
    file_name = remove_space(file_name)
    file_name = remove_tags(file_name)

    file_name = replace_keywords(file_name)
    file_name = rename_edge_cases(file_name)
    file_name = remove_sound_index(file_name)
    file_name = remove_card_name_at_end(file_name)
    file_name = remove_card_name_at_center(file_name)

    file_end = get_file_end(file_name)
    file_start = get_file_start(file_name)

    return file_start + file_end


def replace_keywords(file_name):
    file_name = str.replace(file_name, "_effect", "_Trigger")
    file_name = str.replace(file_name, "_EnterPlay", "_Play")
    file_name = str.replace(file_name, "_CUSTOM", "_Custom")
    file_name = str.replace(file_name, "ALT", "Alternate")
    file_name = str.replace(file_name, "Alt.", "Alternate.")
    file_name = str.replace(file_name, "DEATH", "Death")
    return file_name


def get_file_start(file_name):
    first_index = get_underscore_index(file_name, 0)

    try:
        second_index = get_underscore_index(file_name, first_index + 1)
    except TypeError:
        second_index = None

    if second_index is None:
        file_start = file_name[:first_index]
    else:
        file_start = file_name[:second_index]

    return file_start


def remove_card_name_at_center(file_name):
    index_count = get_underscore_count(file_name)

    try:
        middle_name = get_middle_name(file_name)
    except TypeError:
        middle_name = None

    if index_count is 4:
        file_name = str.replace(file_name, middle_name + "_", "")

    return file_name


def remove_card_name_at_end(file_name):
    start_index = str.rfind(file_name, "_")
    end_index = str.find(file_name, ".ogg")
    name = file_name[start_index:end_index]

    if len(name) > 8 and "Alternate" not in file_name:
        file_name = str.replace(file_name, name, "")

    return file_name


def get_middle_name(file_name):
    first_index = get_underscore_index(file_name, 0)
    second_index = get_underscore_index(file_name, first_index + 1)
    third_index = str.rfind(file_name, "_")

    if second_index is None:
        second_index = third_index
    else:
        second_index += 1

    return file_name[second_index:third_index]


def get_underscore_count(file_name):
    count = 0
    start_index = 0

    while get_underscore_index(file_name, start_index) is not None:
        count += 1
        start_index = get_underscore_index(file_name, start_index) + 1

    return count


def remove_space(file_name):
    if " " in file_name:
        space_index = str.index(file_name, " ")
        next_underscore_index = get_underscore_index(file_name, space_index)
        substring = file_name[space_index:next_underscore_index]
        file_name = str.replace(file_name, substring, "")

    return file_name


def remove_tags(file_name):
    if "VO" in file_name:
        file_name = file_name[3:]
    if "SFX" in file_name or "WoW" in file_name:
        file_name = file_name[4:]
    return file_name


def remove_sound_index(file_name):
    for index in range(0, 8):
        file_name = str.replace(file_name, "_0" + str(index) + ".", ".")
        file_name = str.replace(file_name, str(index) + ".ogg", ".ogg")
    return file_name


def get_file_end(file_name):
    index = str.rfind(file_name, "_")
    return file_name[index:]


def get_underscore_index(file_name, start_index):
    start_index += 1
    try:
        index = str.index(file_name, "_", start_index)
    except ValueError:
        index = None
    return index