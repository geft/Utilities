import cfscrape

import hearthpwn

site_url = "http://www.hearthpwn.com/cards?display=1"


def get_input(text):
    try:
        return int(input(text))
    except TypeError:
        print("Not a number")
        exit()


def get_site_content(url):
    scraper = cfscrape.create_scraper(js_engine="Node")
    return scraper.get(url).text


page_index_start = get_input("Please enter start index: ")
page_index_end = get_input("Please enter end index (not inclusive): ")
hearthpwn.directory.check_output_directories()

for page_index in range(hearthpwn.page.modify_start_index(site_url, page_index_start), page_index_end):
    site_url = hearthpwn.page.modify_page(site_url, page_index, page_index_end)
    site_url = hearthpwn.page.modify_display_type(site_url)

    print("Loading " + site_url)
    hearthpwn.downloader.start_download(get_site_content(site_url), page_index)

hearthpwn.logger.print_log()
