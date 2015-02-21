def reformat_sound_name(file_name):
    file_name = remove_tags(file_name)
    file_name = trim_sound_index(file_name)
    file_end = get_file_end(file_name)

    first_index = get_first_index(file_name)
    second_index = get_underscore_index(file_name, first_index)
    file_name = file_name[:second_index + 1] + file_end

    third_index = get_underscore_index(file_name, second_index)
    if third_index != len(file_name):
        file_name = file_name[:third_index] + ".ogg"

    return file_name


def remove_tags(file_name):
    if "VO" in file_name:
        file_name = file_name[3:]
    if "SFX" in file_name or "WoW" in file_name:
        file_name = file_name[4:]
    return file_name


def trim_sound_index(file_name):
    for index in range(1, 6):
        file_name = str.replace(file_name, "_0" + str(index) + ".", ".")
        file_name = str.replace(file_name, str(index) + ".ogg", ".ogg")
    return file_name


def get_file_end(file_name):
    file_name = str.replace(file_name, "_effect", "_Trigger")
    file_name = str.replace(file_name, "_EnterPlay", "_Play")
    index = str.rfind(file_name, "_") + 1
    return file_name[index:]


def get_first_index(file_name):
    space = "%20"
    if space in file_name:
        first_index = str.index(file_name, space) + len(space)
    else:
        first_index = str.index(file_name, "_") + 1
    return first_index


def get_underscore_index(file_name, start_index):
    try:
        index = str.index(file_name, "_", start_index)
    except ValueError:
        index = len(file_name)
    return index