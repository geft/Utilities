import cfscrape

import hearthpwn

site_url = "http://www.hearthpwn.com/cards?display=1&filter-premium=1&filter-set=105&filter-unreleased=1&page=2"

# download begins from this card
start_index = 0

# download stops at this page (this index is excluded)
page_index_end = 3


def get_site_content(url):
    scraper = cfscrape.create_scraper(js_engine="Node")
    return scraper.get(url).text


def modify_page(url):
    page_modifier = "&page="
    if page_index_end > 1 and page_modifier not in url:
        url += page_modifier + str(page_index)
    if page_modifier + str(page_index - 1) in url:
        url = str.replace(
            url,
            page_modifier + str(page_index - 1),
            page_modifier + str(page_index))

    return url


def modify_display_type(url):
    display_modifier = '&display='

    if display_modifier in url:
        index = url.find(display_modifier) + len(display_modifier)
        url = url[:index] + '1' + url[index + 1:]
    else:
        url = url + display_modifier + '1'

    return url


def modify_start_index():
    page_modifier = '&page='
    if page_modifier in site_url:
        index = site_url.find(page_modifier) + len(page_modifier)

        if site_url[index].isdigit():
            return site_url[index]


# START #

hearthpwn.directory.check_output_directories()

for page_index in range(int(modify_start_index()), page_index_end):
    site_url = modify_page(site_url)
    site_url = modify_display_type(site_url)

    print("Loading " + site_url)
    hearthpwn.downloader.start_download(get_site_content(site_url), start_index, page_index)
