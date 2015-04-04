__author__ = 'Gerry'

import os
import shutil

import hearthhead.reformat_sound


def get_src():
    path = None
    result = None

    while result is None:
        path = input("Enter sounds folder: ")

        if os.path.isdir(path):
            result = True
        else:
            print("Invalid directory")

    return path


def get_dst(src_dir):
    path = os.path.join(os.path.dirname(src_dir), "card_sounds")

    if os.path.isdir(path):
        shutil.rmtree(path)

    while True:
        try:
            os.makedirs(path)
            break
        except PermissionError:
            pass

    return path


src = get_src()
dst = get_dst(src)
file_list = os.listdir(src)

for file_name in file_list:
    src_path = os.path.join(src, file_name)
    new_file_name = hearthhead.reformat_sound.reformat_sound_name(file_name)
    dst_path = os.path.join(dst, new_file_name)

    if os.path.isfile(src_path):
        shutil.copy(src_path, dst_path)