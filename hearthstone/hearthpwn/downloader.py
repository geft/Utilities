import json
import os
import re
import threading
import time
import urllib.error
import urllib.request
from http.client import IncompleteRead
from multiprocessing.dummy import Pool as ThreadPool

import cfscrape

from directory import get_image_path, get_video_path, get_audio_path
from logger import append_log

should_download_image = True
should_download_video = True
should_download_audio = True
should_download_card_back = False

thread_size = 2
site_root = "http://www.hearthpwn.com"
page_pattern = 'manual-data-link\" href=\"(.*?)\"'
card_name_pattern = '<h2 class="caption">(.*)<\/h2>'
json_path = "C:\\Users\\Gerry\\Desktop\\cards.json"

image_extension = ".png"
image_pattern = 'data-imageurl=\"(.*?.png)\"'

video_extension = ".webm"
video_pattern = 'data-animationurl=\"(.*?webm)\"'

audio_pattern = 'src=\"(.*ogg)'
audio_name_pattern = 'sound/(.*ogg)'

card_back_name_pattern = '\d+\/\d+\/(.*)\.'


def does_file_exist(file_path):
    return os.path.isfile(file_path)


def get_pattern(pattern, string):
    match = get_pattern_group(pattern, string)

    if len(match) > 0:
        try:
            return match[0]
        except IndexError:
            pass
    else:
        return None


def get_pattern_group(pattern, string):
    return re.findall(re.compile(pattern), string)


def get_indexed_path(file_path, file_ext):
    if does_file_exist(file_path + file_ext):
        index = 1
        while does_file_exist(file_path + str(index) + file_ext):
            index += 1
        return file_path + str(index) + file_ext
    else:
        return file_path + file_ext


def download_image(name, url):
    path = get_indexed_path(get_image_path() + name, image_extension)
    if url is not None:
        retrieve_url_data(path, name, url, "image")


def download_video(name, url):
    path = get_indexed_path(get_video_path() + name, video_extension)
    if url is not None:
        retrieve_url_data(path, name, url, "video")


def download_audio(id, name, url):
    path = get_audio_path() + id + " - " + name
    if url is not None:
        retrieve_url_data(path, name, url, "audio")


def retrieve_url_data(path, name, url, file_type):
    print(threading.current_thread().name + ": url " + url + " with path " + path)

    while True:
        try:
            urllib.request.urlretrieve(url, path)
            print("Downloaded " + file_type + ": " + name)
            break
        except urllib.error.HTTPError:
            append_log("ERROR: " + name + " with url " + url + " is missing " + file_type)
            break
        except ConnectionResetError:
            print("Failed to download " + name)
            reconnect()


def download_card_back(source):
    group_image = get_pattern_group(image_pattern, source)
    group_video = get_pattern_group(video_pattern, source)

    if len(group_image) > 0:
        for i in range(0, len(group_image)):
            image = group_image[i]
            video = group_video[i]

            name = get_pattern(card_back_name_pattern, image)

            download_image(name, image)
            download_video(name, video)
    else:
        print("Unable to find card back links")


def start_download(source):
    if should_download_card_back:
        download_card_back(source)
    else:
        links = get_pattern_group(page_pattern, source)

        if thread_size <= 1:
            for link in links:
                download(link)
        else:
            pool = ThreadPool(thread_size)
            pool.map(download, links)
            pool.close()
            pool.join()


def download(link):
    while True:
        try:
            source = get_source(link)
            break
        except Exception:
            reconnect()

    card_name = str(get_pattern(card_name_pattern, source)).replace("&#x27;", "'")
    cards = load_json()

    if card_name is None:
        print("Failed to find card name in " + link)
        return

    while cards is not None:
        try:
            i = next((i for i in range(0, len(cards)) if "name" in cards[i] and cards[i]["name"] == card_name), -1)
            j = next((j for j in range(i+1, len(cards)) if "name" in cards[j] and cards[j]["name"] == card_name), -1)

            if i == -1 and j == -1:
                print("Failed to find " + card_name + " in json")
                return
            elif i != -1 and j == -1:
                card_id = cards[i]["id"]
            else:
                card_id = "manual" + cards[i]["id"]

            if should_download_image:
                download_image(card_id, get_pattern(image_pattern, source))

            if should_download_video:
                pattern = get_pattern(video_pattern, source)
                if pattern is not None:
                    download_video(card_id, pattern)

            if should_download_audio:
                group = get_pattern_group(audio_pattern, source)
                for i in range(0, len(group)):
                    url = group[i].replace(" ", "%20")
                    name = group[i].replace(" ", "_")
                    pattern = get_pattern(audio_name_pattern, name)

                    if pattern is not None:
                        download_audio(card_id, pattern, url)
                    else:
                        print("Unable to find audio pattern in " + url)
                        break

            break
        except IncompleteRead or TimeoutError:
            print("Failed to download " + link)
            reconnect()
        except IOError:
            print("Failed to read " + card_name + " in json file")
            break


def get_source(url):
    return cfscrape.create_scraper().get(site_root + url, timeout=10).content.decode("utf-8")


def reconnect():
    print(threading.current_thread().name + ": Connection error. Retrying in a moment...")
    time.sleep(120)
    print(threading.current_thread().name + ": Reconnecting")


def load_json():
    cards = None
    try:
        with open(json_path, 'r', encoding="utf8") as file:
            cards = json.loads(file.read())
    except IOError:
        print("Failed to load " + json_path)
    return cards
