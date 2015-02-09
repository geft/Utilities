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

    if "_01." in file_name or "_02." in file_name or "_03." in file_name:
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

        if "t_" in file_name and "NEW1" in file_name:
            file_name = file_name[:10] + file_end + ".ogg"
        elif "t_" in file_name or "NEW1" in file_name or "DREAM" in file_name:
            file_name = file_name[:9] + file_end + ".ogg"
        else:
            file_name = file_name[:8] + file_end + ".ogg"

    return file_name