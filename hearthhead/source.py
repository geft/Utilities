__author__ = 'Gerry'

import urllib.request
import urllib.error
import time


def is_source_valid(source):
    return source is not ""


def get_source_from_page(page):
    source = None

    while source is None:
        try:
            source = urllib.request.urlopen("http://www.hearthhead.com/card=" + page).read()
        except urllib.error.HTTPError:
            print("Page " + page + " not found")
            return ""
        except urllib.error.URLError:
            time.sleep(300)


    return source.decode("utf-8")

