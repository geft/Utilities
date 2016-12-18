import re
import shutil
import time
import urllib.error
import urllib.request
from multiprocessing.dummy import Pool as ThreadPool

import cutepets.wallpaperscraft.directory

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers = {'User-Agent': user_agent}
image_pattern = '(?:src="\/\/)(.*\.jpg)'
name_pattern = '(?:image\/)(.*)'


def get_pattern(pattern, string):
    match = get_pattern_group(pattern, string)

    if match is not None and len(match) > 0:
        return match[0]
    else:
        return None


def get_pattern_group(pattern, string):
    return re.findall(re.compile(pattern), string)


def get_url_content(url):
    request = urllib.request.Request(url, None, headers)
    response = urllib.request.urlopen(request)
    return response.read().decode("utf-8")


def start_download(page_url):
    links = get_pattern_group(image_pattern, get_url_content(page_url))

    pool = ThreadPool(3)
    pool.map(download, links)
    pool.close()
    pool.join()


def get_large_url(small_url):
    large_url = re.sub('i\d\.', "", small_url)
    large_url = str.replace(large_url, "168x300", "1080x1920")

    return large_url


def download(small_url):
    large_url = get_large_url(small_url)
    name = get_pattern(name_pattern, small_url)

    while True and name is not None:
        try:
            print("Downloading " + large_url)
            download_image(large_url, name)
            return
        except TimeoutError:
            reconnect()


def download_image(url, name):
    request = urllib.request.Request("http://" + url, None, headers)
    response = urllib.request.urlopen(request)

    with response, open(image_path(name), 'wb') as out_file:
        shutil.copyfileobj(response, out_file)


def image_path(name):
    return cutepets.wallpaperscraft.directory.get_image_path() + "\\" + name


def reconnect():
    print("Connection error. Retrying in 30 seconds...")
    time.sleep(30)
