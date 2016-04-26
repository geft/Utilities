import http.client
import time
import traceback
import urllib.error

import id_parser
import scraper
import source


def is_download_sound():
    return True


def is_download_image():
    return False


def reconnect(current_page):
    print("Error obtaining page " + current_page)
    print("Connection error. Retrying in 5 minutes...")
    time.sleep(300)


id_list = id_parser.get_id_from_url()

if id_list is not None:
    for page in id_list:
        page = str(page)

        result = None
        while result is None:
            try:
                sourceFile = source.get_source_from_page(page)
                if source.is_source_valid(sourceFile):
                    scraper.start(sourceFile)
                    print("Page " + page + " scraped")
                result = True
            except ValueError:
                print(traceback.format_exc())
                exit()
            except http.client.IncompleteRead:
                pass
            except TimeoutError:
                reconnect(page)
            except urllib.error.URLError:
                reconnect(page)
