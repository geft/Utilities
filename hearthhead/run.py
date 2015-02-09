__author__ = 'Gerry'

import sys
import time

import hearthhead.source
import hearthhead.scraper


def validate_start():
    global start
    try:
        start = int(start)
    except ValueError:
        sys.exit(str(start) + " is not a valid number")
    if start >= end:
        sys.exit(str(start) + " cannot be bigger than " + str(end))


start = input("Enter starting index: ")
end = 3000
validate_start()


for page in range(start, end):
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
                print("Error scraping page " + page)
        except Exception:
            print("Connection error. Retrying in 5 minutes...")
            time.sleep(300)