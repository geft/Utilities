# extract all card images from HearthPwn, only works with display mode = 1

import os
import re
import time
import urllib.request

site_root = "http://www.hearthpwn.com"
# page index is calculated below and should be left out
site_url = "http://www.hearthpwn.com/cards?display=1&filter-premium=1&filter-set=104"
page_index_end = 1

page_pattern = 'manual-data-link\" href=\"(.*?)\"'
card_name_pattern = '<a href=\"/cards/\d\d\d\d\d-(.*?)\" rel=\"up\"'
image_pattern = 'data-imageurl=\"(.*?.png)\"'
video_pattern = 'data-animationurl=\"(.*?webm)\"'

path = "C:\\Users\\Gerry\\Desktop\\image\\"
path_video = "C:\\Users\\Gerry\\Desktop\\video\\"


def get_url_content(url):
    return urllib.request.urlopen(url).read().decode("utf-8")


def does_file_exist(file_path):
    return os.path.isfile(file_path)


def check_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def get_pattern(pattern, string, index=0):
    match = re.findall(re.compile(pattern), string)

    if match:
        try:
            return match[index]
        except IndexError:
            pass

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
        indexed_path = get_indexed_path(path + name, ".png")
        urllib.request.urlretrieve(url, indexed_path)
        print("Downloaded image: " + name)


def download_video(name, url):
    if url and not url.endswith(".png"):
        indexed_path = get_indexed_path(path_video + name, ".webm")
        urllib.request.urlretrieve(url, indexed_path)
        print("Downloaded animation: " + name)


def reconnect():
    print("Connection error. Retrying in 1 minute...")
    time.sleep(60)

check_directory(path)
check_directory(path_video)

for page_index in range(1, page_index_end + 1):

    # use page index
    # site = get_url_content(site_url + str(page_index))

    # specific page only
    site = get_url_content(site_url)

    # change this to start from a specific card on the page
    num = 0

    link = get_pattern(page_pattern, site, num)

    while link is not None:
        page = get_url_content(site_root + link)

        card_name = str(get_pattern(card_name_pattern, page))
        print("Page " + str(page_index) + ", Index " + str(num))

        success = False
        while success is False:
            try:
                download_image(card_name, get_pattern(image_pattern, page))
                download_video(card_name, get_pattern(video_pattern, page))
                success = True
            except TimeoutError:
                reconnect()

        num += 1
        link = get_pattern(page_pattern, site, num)

