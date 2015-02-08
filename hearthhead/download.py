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
    urllib.request.urlretrieve(url, path)


def reformat_sound_name(file_name):
    file_name = str.replace(file_name, "EnterPlay", "Play")

    if file_name[0:3] is "VO_":
        file_name = file_name[3:]

    if file_name[0:3] is "SFX":
        file_name = file_name[4:]

    if "_01" in file_name or "_02" in file_name or "_03" in file_name:
        file_name = file_name[:-7] + ".ogg"

    if len(file_name) > 20:
        if "Attack" in file_name:
            file_end = "Attack"
        elif "Death" in file_name:
            file_end = "Death"
        else:
            file_end = "Play"

        file_name = file_name[:8] + file_end + ".ogg"

    return file_name