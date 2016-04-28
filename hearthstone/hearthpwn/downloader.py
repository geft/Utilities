import os
import re
import time
import urllib.request

import hearthpwn.directory

site_root = "http://www.hearthpwn.com"
page_pattern = 'manual-data-link\" href=\"(.*?)\"'
card_name_pattern = '<a href=\"/cards/\d\d\d\d\d-(.*?)\" rel=\"up\"'

image_extension = ".png"
image_pattern = 'data-imageurl=\"(.*?.png)\"'

video_extension = ".webm"
video_pattern = 'data-animationurl=\"(.*?webm)\"'


def does_file_exist(file_path):
    return os.path.isfile(file_path)


def get_pattern(pattern, string, index=0):
    try:
        match = re.findall(re.compile(pattern), string)

        if match:
            try:
                return match[index]
            except IndexError:
                pass
    except TypeError:
        print('Error with pattern ' + pattern)
        print(string)

    return None


def get_indexed_path(file_path, file_ext):
    if does_file_exist(file_path + file_ext):
        index = 1
        while does_file_exist(file_path + str(index) + file_ext):
            index += 1
        return file_path + str(index) + file_ext
    else:
        return file_path + file_ext


def download_image(name, url):
    if url is not None:
        indexed_path = get_indexed_path(hearthpwn.directory.get_image_path() + name, image_extension)
        retrieve_url_data(indexed_path, name, url)


def retrieve_url_data(indexed_path, name, url):
    print("Processing url " + url + " with index path " + str(indexed_path))
    urllib.request.urlretrieve(url, indexed_path)
    print("Downloaded image: " + name)


def download_video(name, url):
    if url and not url.endswith(image_extension):
        indexed_path = get_indexed_path(hearthpwn.directory.get_video_path() + name, video_extension)
        retrieve_url_data(indexed_path, name, url)


def get_url_content(url):
    return urllib.request.urlopen(url).read().decode("utf-8")


def start_download(site, start_index, page_index):
    link = get_pattern(page_pattern, site, start_index)

    while link is not None:
        page = get_url_content(site_root + link)

        card_name = str(get_pattern(card_name_pattern, page))
        print("Page " + str(page_index) + ", Index " + str(start_index))

        success = False
        while success is False:
            try:
                download_image(card_name, get_pattern(image_pattern, page))
                download_video(card_name, get_pattern(video_pattern, page))
                success = True
            except TimeoutError:
                reconnect()

        start_index += 1
        link = get_pattern(page_pattern, site, start_index)


def reconnect():
    print("Connection error. Retrying in 1 minute...")
    time.sleep(60)
