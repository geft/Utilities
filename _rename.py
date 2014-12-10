import os

baseDir = r"C:\Users\Gerry\Downloads\New folder"

for folderName in os.listdir(baseDir):
	if folderName.startswith("Read"):
		os.rename(os.path.join(baseDir, folderName),
			os.path.join(baseDir, folderName[5:-10]))
	elif folderName.startswith("Page"):
		subFolder = os.path.join(baseDir, folderName)
		for fileName in os.listdir(subFolder):
			if fileName[-6] is "-":
				os.rename(os.path.join(subFolder, fileName),
					os.path.join(subFolder,
					fileName[:-5] + "00" + fileName[-5:]))
			elif fileName[-7] is "-":
				os.rename(os.path.join(subFolder, fileName),
					os.path.join(subFolder,
					fileName[:-6] + "0" + fileName[-6:]))
		os.rename(os.path.join(baseDir, folderName),
			os.path.join(baseDir, folderName[9:-57]))