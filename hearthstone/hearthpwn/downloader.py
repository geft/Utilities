import json
import os
import re
import threading
import time
import urllib.error
import urllib.request
from http.client import IncompleteRead
from multiprocessing.dummy import Pool as ThreadPool

from directory import get_image_path, get_video_path, get_audio_path
from logger import append_log

should_download_image = True
should_download_video = True
should_download_audio = True

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
    if url is not None and not url.endswith(image_extension):
        retrieve_url_data(path, name, url, "video")


def download_audio(id, name, url):
    path = get_audio_path() + id + "_" + name
    if url is not None:
        retrieve_url_data(path, name, url, "audio")


def retrieve_url_data(path, name, url, file_type):
    print(threading.current_thread().name + ": url " + url + " with path " + path)

    success = False
    while not success:
        try:
            urllib.request.urlretrieve(url, path)
            print("Downloaded " + file_type + ": " + name)
            success = True
        except urllib.error.HTTPError:
            append_log("ERROR: " + name + " with url " + url + " is missing " + file_type)
        except ConnectionResetError:
            print("Failed to download " + name)
            reconnect()


def get_url_content(url):
    return urllib.request.urlopen(url).read().decode("utf-8")


def start_download(source):
    links = get_pattern_group(page_pattern, source)

    pool = ThreadPool(4)
    pool.map(download, links)
    pool.close()
    pool.join()


def download(link):
    success = False

    source = get_source(link)
    card_name = str(get_pattern(card_name_pattern, source)).replace("&#x27;", "'")
    cards = load_json()

    if card_name is None:
        print("Failed to find card name in " + link)
        return

    try:
        while success is False and cards is not None:
            i = next((i for i in range(0, len(cards)) if "name" in cards[i] and cards[i]["name"] == card_name), -1)
            j = next((j for j in range(i+1, len(cards)-i-1) if "name" in cards[j] and cards[j]["name"] == card_name), -1)

            if i == -1:
                print("Failed to find " + card_name + " in json")
                break
            elif i != -1 and j != -1 and i != j:
                card_id = "manual" + cards[i]["id"]
            else:
                card_id = cards[i]["id"]

            if should_download_image:
                download_image(card_id, get_pattern(image_pattern, source))

            if should_download_video:
                download_video(card_id, get_pattern(video_pattern, source))

            if should_download_audio:
                group = get_pattern_group(audio_pattern, source)
                for i in range(0, len(group)):
                    url = group[i].replace(" ", "%20")
                    name = group[i].replace(" ", "_")
                    download_audio(card_id, get_pattern(audio_name_pattern, name), url)

            success = True
    except IncompleteRead or TimeoutError:
        print("Failed to download " + link)
        reconnect()
    except IOError:
        print("Failed to read " + card_name + " in json file")


def get_source(link):
    source = None
    while source is None:
        try:
            source = get_url_content(site_root + link)
        except ConnectionResetError:
            reconnect()
    return source


def reconnect():
    print(threading.current_thread().name + ": Connection error. Retrying in 1 minute...")
    time.sleep(60)


def load_json():
    cards = None
    try:
        with open(json_path, 'r', encoding="utf8") as file:
            cards = json.loads(file.read())
    except IOError:
        print("Failed to load " + json_path)
    return cards
