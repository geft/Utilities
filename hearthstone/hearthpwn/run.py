import cfscrape

import directory
import downloader
import logger
import page

site_url = "http://www.hearthpwn.com/cards?display=1&filter-include-card-text=y&filter-set=18"
content = 'Add content here'

def get_input(text):
    try:
        return int(input(text))
    except TypeError:
        print("Not a number")
        exit()


def get_site_content(url):
    scraper = cfscrape.create_scraper(js_engine="Node")
    return scraper.get(url).text


directory.check_output_directories()

# page_index_end = get_input("Enter end index: ")
page_index_end = 2

for page_index in range(1, page_index_end):
    site_url = page.modify_display_type(site_url)
    site_url = page.modify_page(site_url, page_index, page_index_end)

    print("Loading " + site_url)

    # content = get_site_content(site_url)
    downloader.start_download(content, page_index)

logger.print_log()
