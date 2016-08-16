import urllib.error
import urllib.request
from multiprocessing.dummy import Pool as ThreadPool

import hearthstone.hearthpedia as hearthpedia

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers = {'User-Agent': user_agent,}


def get_site(url):
    try:
        request = urllib.request.Request(url, None, headers)
        return urllib.request.urlopen(request).read().decode('utf-8')
    except urllib.error.HTTPError:
        print('URL not found')
        exit()


def download_url_list(url_list):
    pool = ThreadPool(4)
    pool.map(download, url_list)
    pool.close()
    pool.join()


def download(url):
    print('Processing ' + url)
    name = hearthpedia.formatter.get_name(url)

    try:
        urllib.request.urlretrieve(url, hearthpedia.directory.path + name + '.png')
        print(name + ' downloaded')
    except urllib.error.HTTPError:
        print(name + ' not found')
