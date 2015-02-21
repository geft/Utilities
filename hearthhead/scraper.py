import hearthhead.download


def start(source):
    download_sound(source)
    download_animation(source)

    return 0


def download_sound(source):
    for index in range(0, 4):
        if has_sound(source, index):
            hearthhead.download.sound(get_sound_url(source, index))


def download_animation(source):
    try:
        hearthhead.download.animated(get_gif_url(source))
    except ValueError:
        print("No animation found")


def get_sound_url(source, num):
    sub_id = "cardsound" + str(num)
    sub_start = 'src="//'
    sub_end = '.ogg'
    return get_url(source, sub_id, sub_start, sub_end)


def get_gif_url(source):
    sub_id = "tooltip_premium_enus"
    sub_start = 'src="//'
    sub_end = ".gif"

    return get_url(source, sub_id, sub_start, sub_end)


def get_url(source, sub_id, sub_start, sub_end):
    id_index = str.index(source, sub_id)
    file_start = str.index(source, sub_start, id_index) + len(sub_start)
    file_end = str.index(source, sub_end, file_start) + len(sub_end)
    file_url = source[file_start:file_end]
    print(file_url)
    return "http://" + file_url


def has_sound(source, index):
    sub = "cardsound" + str(index)
    try:
        str.index(source, sub)
    except ValueError:
        return False
    return True