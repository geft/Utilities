import os
import re
import time
import urllib.error
import urllib.request
from multiprocessing.dummy import Pool as ThreadPool

from hearthstone.hearthpwn.directory import get_image_path, get_video_path
from hearthstone.hearthpwn.logger import append_log

site_root = "http://www.hearthpwn.com"
card_name_pattern = '<link rel="canonical" href="http:\/\/www.hearthpwn.com\/cards\/[0-9]+-(.*?)\"'

image_extension = ".png"
image_pattern = 'data-imageurl=\"(.*?.png)\"'

video_extension = ".webm"
video_pattern = 'data-animationurl=\"(.*?webm)\"'


def get_page_pattern(set_number):
    return 'set-' + str(set_number) + ' manual-data-link\" href=\"(.*?)\"'


def does_file_exist(file_path):
    return os.path.isfile(file_path)


def get_pattern(pattern, string, index=0):
    match = re.findall(re.compile(pattern), string)

    if len(match) > 0:
        try:
            return match[index]
        except IndexError:
            pass
    else:
        return None


def get_pattern_group(string, set_number):
    return re.findall(re.compile(get_page_pattern(set_number)), string)


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
        indexed_path = get_indexed_path(get_image_path() + name, image_extension)
        retrieve_url_data(indexed_path, name, url, "image")


def retrieve_url_data(indexed_path, name, url, file_type):
    print("Processing url " + url + " with index path " + str(indexed_path))
    try:
        urllib.request.urlretrieve(url, indexed_path)
    except urllib.error.HTTPError:
        append_log("ERROR: " + name + " with url " + url + " is missing " + file_type)

    print("Downloaded " + file_type + ": " + name)


def download_video(name, url):
    if url and not url.endswith(image_extension):
        indexed_path = get_indexed_path(get_video_path() + name, video_extension)
        retrieve_url_data(indexed_path, name, url, "video")


def get_url_content(url):
    return urllib.request.urlopen(url).read().decode("utf-8")


def start_download(site, page_index, set_number):
    links = get_pattern_group(site, set_number)
    print("Processing page " + str(page_index))

    pool = ThreadPool(4)
    pool.map(download, links)
    pool.close()
    pool.join()


def download(link):
    page = get_url_content(site_root + link)
    card_name = str(get_pattern(card_name_pattern, page))
    success = False
    while success is False:
        try:
            download_image(card_name, get_pattern(image_pattern, page))
            download_video(card_name, get_pattern(video_pattern, page))
            success = True
        except TimeoutError:
            reconnect()


def reconnect():
    print("Connection error. Retrying in 1 minute...")
    time.sleep(60)
