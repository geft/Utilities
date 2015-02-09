__author__ = 'Gerry'

import hearthhead.download


def start(source):
    if has_sound(source):
        hearthhead.download.sound(get_sound_url(source, 0))
        hearthhead.download.sound(get_sound_url(source, 1))
        hearthhead.download.sound(get_sound_url(source, 2))

        if has_trigger(source):
            hearthhead.download.sound(get_sound_url(source, 3))

            # hearthhead.download.animated(get_gif_url(source))


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


def has_sound(source):
    sub = "cardsound"
    try:
        str.index(source, sub)
    except ValueError:
        return False
    return True


def has_trigger(source):
    sub = "cardsound3"
    try:
        str.index(source, sub)
    except ValueError:
        return False
    return True
