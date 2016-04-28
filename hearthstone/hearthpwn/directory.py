import os

path_image = "C:\\Users\\Gerry\\Desktop\\image\\"
path_video = "C:\\Users\\Gerry\\Desktop\\video\\"


def check_output_directories():
    check(path_image)
    check(path_video)


def check(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def get_image_path():
    return path_image


def get_video_path():
    return path_video
