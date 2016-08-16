import http.client
import traceback
import urllib.error

import hearthstone.hearthhead as hearthhead


def is_download_sound():
    return True


def is_download_image():
    return False


def print_error(current_page):
    print("Error obtaining page " + current_page)


def get_log(current_page, current_log):
    return current_log + "\n" + current_page


id_list = hearthhead.id_parser.get_id_from_url()
log = "Error on the following pages: "

if id_list is not None:
    for page in id_list:
        page = str(page)

        try:
            sourceFile = hearthhead.source.get_source_from_page(page)
            if hearthhead.source.is_source_valid(sourceFile):
                hearthhead.scraper.start(
                    sourceFile, is_download_sound(), is_download_image())
            result = True

        except ValueError:
            print(traceback.format_exc())
            exit()
        except http.client.IncompleteRead:
            print_error(page)
            log = get_log(page, log)
        except TimeoutError:
            print_error(page)
            log = get_log(page, log)
        except urllib.error.URLError:
            print_error(page)
            log = get_log(page, log)

        print("Page " + page + " scraped")

print(log)
