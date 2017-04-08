import os
import shutil

path_image = "C:\\Users\\Gerry\\Desktop\\image\\"
path_video = "C:\\Users\\Gerry\\Desktop\\video\\"
path_audio = "C:\\Users\\Gerry\\Desktop\\audio\\"


def check_output_directories():
    check(path_image)
    check(path_video)
    check(path_audio)


def check(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory, ignore_errors=True)

    os.makedirs(directory)


def get_image_path():
    return path_image


def get_video_path():
    return path_video


def get_audio_path():
    return path_audio
