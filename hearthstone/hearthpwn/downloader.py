import os
import re
import time
import urllib.request
import urllib.error
from http.client import IncompleteRead

from multiprocessing.dummy import Pool as ThreadPool
from directory import get_image_path, get_video_path, get_audio_path
from logger import append_log

should_download_image = True
should_download_video = True
should_download_audio = True

site_root = "http://www.hearthpwn.com"
page_pattern = 'manual-data-link\" href=\"(.*?)\"'
card_name_pattern = '<link rel="canonical" href="http:\/\/www.hearthpwn.com\/cards\/[0-9]+-(.*?)\"'

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


def download_audio(name, url):
    path = get_audio_path() + name
    if url is not None:
        retrieve_url_data(path, name, url, "audio")


def retrieve_url_data(path, name, url, file_type):
    print("Processing url " + url + " with path " + path)

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

    pool = ThreadPool(3)
    pool.map(download, links)
    pool.close()
    pool.join()


def download(link):
    success = False

    try:
        while success is False:
            source = get_url_content(site_root + link)
            card_name = str(get_pattern(card_name_pattern, source))

            if should_download_image:
                download_image(card_name, get_pattern(image_pattern, source))

            if should_download_video:
                download_video(card_name, get_pattern(video_pattern, source))

            if should_download_audio:
                group = get_pattern_group(audio_pattern, source)
                for i in range(0, len(group)):
                    url = group[i].replace(" ", "%20")
                    name = group[i].replace(" ", "_")
                    download_audio(get_pattern(audio_name_pattern, name), url)

            success = True
    except IncompleteRead or ConnectionResetError or TimeoutError:
        print("Failed to download " + link)
        reconnect()


def reconnect():
    print("Connection error. Retrying in 1 minute...")
    time.sleep(60)
