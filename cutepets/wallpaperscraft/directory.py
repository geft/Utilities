import os

image_path = "C:\\Users\\Gerry\\Desktop\\images\\"


def get_image_path():
    if not os.path.exists(image_path):
        os.makedirs(image_path)

    return image_path
