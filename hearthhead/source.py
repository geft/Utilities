__author__ = 'Gerry'

import urllib.request


def is_source_valid(source):
    return source is not ""


def get_source_from_page(page):
    source = urllib.request.urlopen("http://www.hearthhead.com/card=" + page).read()
    return source.decode("utf-8")

