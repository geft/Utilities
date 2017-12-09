from directory import check_output_directories
from downloader import start_download

# Add source code to content.txt along with cards.json to the desktop
content_path = "C:\\Users\\Gerry\\Desktop\\content.txt"

with open(content_path, 'r') as file:
    content = file.read().replace('\n', '')
    check_output_directories()
    start_download(content)