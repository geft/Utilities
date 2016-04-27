import re

from hearthhead import source


def source_parser(source_text):
    return re.findall(r'\d+(?=,"im)', source_text)


def get_id_from_url():
    url_input = input("Enter URL address: ")
    source_file = source.get_source_from_url(url_input)

    if source_file is "":
        print("Invalid URL")
    else:
        print("Source code obtained")
        return source_parser(source_file)
