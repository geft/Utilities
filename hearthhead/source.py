__author__ = 'Gerry'

import urllib.request
import urllib.error


def is_source_valid(source):
    return source is not ""


def get_source_from_page(page):
    try:
        source = urllib.request.urlopen("http://www.hearthhead.com/card=" + page).read()
    except urllib.error.HTTPError:
        print("Page " + page + " not found")
        return ""


    return source.decode("utf-8")

