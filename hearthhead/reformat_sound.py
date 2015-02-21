def reformat_sound_name(file_name):
    file_name = remove_space(file_name)
    file_name = remove_tags(file_name)
    file_name = remove_sound_index(file_name)
    file_name = remove_card_name(file_name)

    return file_name


def remove_card_name(file_name):
    index_count = get_underscore_count(file_name)

    if index_count is 3:
        last_index = str.rfind(file_name, "_")
        file_name = file_name[:last_index] + ".ogg"

    return file_name


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
    for index in range(0, 6):
        file_name = str.replace(file_name, "_0" + str(index) + ".", ".")
        file_name = str.replace(file_name, str(index) + ".ogg", ".ogg")
    return file_name


def get_file_end(file_name):
    file_name = str.replace(file_name, "_effect", "_Trigger")
    file_name = str.replace(file_name, "_EnterPlay", "_Play")
    index = str.rfind(file_name, "_") + 1
    return file_name[index:]


def get_underscore_index(file_name, start_index):
    start_index += 1
    try:
        index = str.index(file_name, "_", start_index)
    except ValueError:
        index = None
    return index