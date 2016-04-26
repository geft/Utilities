import http.client
import traceback
import urllib.error

import id_parser
import scraper
import source


def is_download_sound():
    return True


def is_download_image():
    return False


def print_error(current_page):
    print("Error obtaining page " + current_page)


id_list = id_parser.get_id_from_url()

if id_list is not None:
    for page in id_list:
        page = str(page)

        try:
            sourceFile = source.get_source_from_page(page)
            if source.is_source_valid(sourceFile):
                scraper.start(
                    sourceFile, is_download_sound(), is_download_image())
                print("Page " + page + " scraped")
            result = True
        except ValueError:
            print(traceback.format_exc())
            exit()
        except http.client.IncompleteRead:
            print_error(page)
        except TimeoutError:
            print_error(page)
        except urllib.error.URLError:
            print_error(page)
