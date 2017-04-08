from directory import check_output_directories
from downloader import start_download

content_path = "C:\\Users\\Gerry\\Desktop\\content.txt"

try:
    with open(content_path, 'r') as file:
        content = file.read().replace('\n', '')
        check_output_directories()
        start_download(content)
except IOError:
    print(content_path + " not found")