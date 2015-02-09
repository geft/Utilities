__author__ = 'Gerry'

import urllib.request
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


def reformat_sound_name(file_name):
    file_name = str.replace(file_name, "EnterPlay", "Play")

    if "VO" in file_name:
        file_name = file_name[3:]

    if "SFX" in file_name or "WoW" in file_name:
        file_name = file_name[4:]

    file_name = str.replace(file_name, "_01.", ".")
    file_name = str.replace(file_name, "_02.", ".")
    file_name = str.replace(file_name, "_03.", ".")

    if len(file_name) > 20:
        if "Attack" in file_name:
            file_end = "Attack"
        elif "Death" in file_name:
            file_end = "Death"
        else:
            file_end = "Play"

        first_index = str.index(file_name, "_") + 1
        second_index = str.index(file_name, "_", first_index) + 1
        file_name = file_name[:second_index] + file_end + ".ogg"

    return file_name