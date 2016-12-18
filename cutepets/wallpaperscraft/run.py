import cutepets.wallpaperscraft.downloader

startPage = 1
endPage = 35
baseUrl = 'http://wallpaperscraft.com/tag/puppy/1080x1920'

for page in range(startPage, endPage + 1):
    if page > 1:
        baseUrlWithPage = baseUrl + "/page" + str(page)
    else:
        baseUrlWithPage = baseUrl

    print("Downloading URL = " + baseUrlWithPage)

    cutepets.wallpaperscraft.downloader.start_download(baseUrlWithPage)
