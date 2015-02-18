# extract all card images from a page in HearthPwn, using display = 2

import urllib.request
import os


def does_file_exist(card_name):
    return os.path.isfile(cwd + "\\" + card_name + ".png")


def download(card_name):
    urllib.request.urlretrieve(cardURL, cwd + "\\" + card_name + ".png")


def remove_num_in_name(card_name):
    return cardName[card_name.find("-") + 1:]


for page in range(1, 9):
    site_raw = urllib.request.urlopen("http://www.hearthpwn.com/cards?display=2&page=" + str(page)).read()
    site = site_raw.decode("utf-8")

    imageStart = "data-imageurl=\""
    imageEnd = "\""
    nameStart = "<h3><a href=\"/cards/"

    index1 = 0
    index2 = 0

    cwd = os.getcwd()
    while True:
        # find the start of image url
        index1 = site.find(imageStart, index1)

        # find the end of image url
        if index1 != -1:
            index2 = site.find(imageEnd, index1 + len(imageStart))

        # break when no more images found
        else:
            break

        # find the start of card name
        if index2 != -1:
            cardURL = site[index1 + len(imageStart): index2]
            indexName1 = site.find(nameStart, index2)

            # find the end of card name
            if indexName1 != -1:
                indexName2 = site.find(imageEnd, indexName1 + len(nameStart))
                cardName = site[indexName1 + len(nameStart): indexName2]

                cardName = remove_num_in_name(cardName)

                # rename file if it exists
                if does_file_exist(cardName):
                    num = 1

                    while does_file_exist(cardName + str(num)):
                        num += 1

                    download(cardName + str(num))
                else:
                    download(cardName)

                index1 = indexName2

            else:
                break