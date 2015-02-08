__author__ = 'Gerry'

import hearthhead.source
import hearthhead.scraper

for page in range(205, 3000):
    page = str(page)
    source = hearthhead.source.get_source_from_page(page)
    if hearthhead.source.is_source_valid(source):
        try:
            hearthhead.scraper.start(source)
        except ValueError:
            print("Error scraping page " + page)

        print("Page " + page + " scraped")