__author__ = 'Gerry'

import time
import traceback
import urllib.error
import http.client

import hearthhead.source
import hearthhead.scraper
import hearthhead.id_parser


def reconnect():
    print("Connection error. Retrying in 5 minutes...")
    time.sleep(300)


id_list = hearthhead.id_parser.get_id_from_url()

if id_list is not None:
    for page in id_list:
        page = str(page)

        result = None
        while result is None:
            try:
                source = hearthhead.source.get_source_from_page(page)
                if hearthhead.source.is_source_valid(source):
                    hearthhead.scraper.start(source)
                    print("Page " + page + " scraped")
                result = True
            except ValueError:
                print(traceback.format_exc())
                exit()
            except http.client.IncompleteRead:
                pass
            except TimeoutError:
                reconnect()
            except urllib.error.URLError:
                reconnect()