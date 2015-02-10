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
    file_name = str.replace(file_name, "_01.", ".")
    file_name = str.replace(file_name, "_02.", ".")
    file_name = str.replace(file_name, "_03.", ".")
    file_name = str.replace(file_name, "_04.", ".")
    return file_name


def reformat_sound_name(file_name):
    if "VO" in file_name:
        file_name = file_name[3:]

    if "SFX" in file_name or "WoW" in file_name:
        file_name = file_name[4:]

    file_name = trim_sound_index(file_name)

    if "_Attack" in file_name:
        file_end = "Attack"
    elif "_Death" in file_name:
        file_end = "Death"
    elif "_Trigger" in file_name or "_Other" in file_name:
        file_end = "Trigger"
    elif "_Play" in file_name or "_EnterPlay" in file_name:
        file_end = "Play"
    else:
        file_end = "Unknown"

    space = "%20"
    if space in file_name:
        first_index = str.index(file_name, space) + len(space)
    else:
        first_index = str.index(file_name, "_") + 1

    second_index = str.index(file_name, "_", first_index) + 1
    file_name = file_name[:second_index] + file_end + ".ogg"

    return file_name