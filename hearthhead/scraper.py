import download
import run


def start(source):
    if run.is_download_sound():
        download_sound(source)

    if run.is_download_image():
        download_image(source)


def download_sound(source):
    for index in range(0, 4):
        if has_sound(source, index):
            download.sound(get_sound_url(source, index))


def download_image(source):
    try:
        download.image(get_png_url(source))
    except ValueError:
        print("No image found")


def get_sound_url(source, num):
    sub_id = "cardsound" + str(num)
    sub_start = 'type="audio/ogg; codecs=&quot;vorbis&quot;"><source src="//'
    sub_end = '.mp3'
    return get_url(source, sub_id, sub_start, sub_end)


def get_png_url(source):
    sub_id = "tooltip_enus"
    sub_start = 'src="//'
    sub_end = ".png"

    return get_url(source, sub_id, sub_start, sub_end)


def get_url(source, sub_id, sub_start, sub_end):
    id_index = str.index(source, sub_id)
    file_start = str.index(source, sub_start, id_index) + len(sub_start)
    file_end = str.index(source, sub_end, file_start) + len(sub_end)
    file_url = source[file_start:file_end]
    print(file_url)

    full_url = "http://" + file_url

    print("Downloading " + full_url)

    return full_url


def has_sound(source, index):
    sub = "cardsound" + str(index)
    try:
        str.index(source, sub)
    except ValueError:
        return False
    return True
