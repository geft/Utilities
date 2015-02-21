__author__ = 'Gerry'

import urllib.request
import urllib.error
import os


def sound(url):
    dir_name = "sounds/"
    file_name = url[str.index(url, dir_name) + len(dir_name):]
    file_name = reformat_sound_name(file_name)
    save(url, dir_name, file_name)


def animated(url):
    dir_name = "animated/"
    file_name = url[str.index(url, dir_name) + len(dir_name):]
    save(url, dir_name, file_name[:-12] + ".gif")


def save(url, dir_name, file_name):
    dir_name = "C:\\Users\\Gerry\\Desktop\\" + dir_name[:-1]
    path = dir_name + "\\" + file_name
    os.makedirs(dir_name, exist_ok=True)
    url = str.replace(url, " ", "%20")
    urllib.request.urlretrieve(url, path)


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


def reformat_sound_name(file_name):
    if "VO" in file_name:
        file_name = file_name[3:]

    if "SFX" in file_name or "WoW" in file_name:
        file_name = file_name[4:]

    file_name = trim_sound_index(file_name)
    file_end = get_file_end(file_name)

    first_index = get_first_index(file_name)

    try:
        second_index = str.index(file_name, "_", first_index) + 1
    except ValueError:
        second_index = len(file_name)

    file_name = file_name[:second_index] + file_end

    return file_name