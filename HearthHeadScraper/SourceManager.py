__author__ = 'Gerry'

import urllib.request


def is_source_valid(source):
    error = "This Hearthstone card doesn't exist."
    return error not in source


def get_source_from_page(page):
    source = urllib.request.urlopen("http://www.hearthhead.com/card=" + str(page)).read()
    return source.decode("utf-8")

