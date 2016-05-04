import os
import shutil

path = 'C:\\Users\\Gerry\\Desktop\\credits\\'


def check():
    if os.path.exists(path):
        shutil.rmtree(path, ignore_errors=True)

    os.makedirs(path)


def get_path():
    return path
