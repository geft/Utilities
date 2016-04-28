import cfscrape

import hearthpwn

# should not include page index
# display mode should be 1
site_url = "http://www.hearthpwn.com//cards?filter-premium=1&filter-set=105&filter-unreleased=1&display=1"

# download begins from this card
start_index = 11

# download stops at this page (this index is excluded)
page_index_end = 3


def get_site_content(url):
    scraper = cfscrape.create_scraper(js_engine="Node")
    return scraper.get(url).text


def check_url():
    if "&display=1" not in site_url:
        print("Display must be set to 1")
        exit()


check_url()
hearthpwn.directory.check_output_directories()

for page_index in range(1, page_index_end):

    if page_index_end > 1:
        site_url += "&page=" + str(page_index)

    hearthpwn.downloader.start_download(get_site_content(site_url), start_index, page_index)
