# extract all card images from a page in HearthPwn, using display = 2

import urllib.request
import os

for page in range(1,9):
	siteb = urllib.request.urlopen("http://www.hearthpwn.com/cards?display=2&page=" + str(page)).read()
	site = siteb.decode("utf-8")

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
			cardURL = site[index1 + len(imageStart) : index2]
			indexName1 = site.find(nameStart, index2)
			
			# find the end of card name
			if indexName1 != -1:
				indexName2 = site.find(imageEnd, indexName1 + len(nameStart))
				cardName = site[indexName1 + len(nameStart) : indexName2]
				
				# remove preceding number from card name
				cardName = cardName[cardName.find("-") + 1 : ]

				# retrieve image into local directory
				isExist = os.path.isfile(cwd + "\\" + cardName + ".png")
				
				num = 0
				
				# rename file if it exists
				if isExist:
					while isExist:
						isExist = os.path.isfile(cwd + "\\" + cardName + str(num) + ".png")
						num += 1
						
					urllib.request.urlretrieve(cardURL, cwd + "\\" + cardName + str(num) + ".png")
				else:
					urllib.request.urlretrieve(cardURL, cwd + "\\" + cardName + ".png")
					
				index1 = indexName2
				
			else:
				break