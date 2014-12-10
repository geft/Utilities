import os

baseDir = os.path.dirname(__file__)

for fileName in ((os.listdir(baseDir))):
	if fileName.endswith('Staff Picks on Vimeo.mp4'):
		os.rename(os.path.join(baseDir, fileName),
			os.path.join(baseDir,
			fileName[:-34] + '.mp4'))
	elif fileName.endswith('Vimeo.mp4'):
		os.rename(os.path.join(baseDir, fileName),
			os.path.join(baseDir,
			fileName[:-13] + '.mp4'))