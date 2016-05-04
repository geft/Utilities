import hearthpedia

url = 'http://hearthstone.gamepedia.com/Credits_card'

hearthpedia.directory.check()
site = hearthpedia.downloader.get_site(url)
url_list = hearthpedia.formatter.get_image_list(site)
url_list = hearthpedia.formatter.get_formatted_url_list(url_list)
hearthpedia.downloader.download_url_list(url_list)
