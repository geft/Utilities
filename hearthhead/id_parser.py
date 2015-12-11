__author__ = 'Gerry'

import re

import hearthhead.source


def source_parser(source_text):
    return re.findall(r'\d+(?=,"im)', source_text)


def get_id_from_url():
    url_input = input("Enter URL address: ")
    source = hearthhead.source.get_source_from_url(url_input)

    if source is "":
        print("Invalid URL")
    else:
        print("Source code obtained")
        return source_parser(source)