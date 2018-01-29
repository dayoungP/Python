import os
from PIL import Image

#get the directory name
dirname = raw_input('directory:\t')
#get the list of jpg file names
picNames = []
for file in os.listdir(r'{0}'.format(dirname)):
	if ("_sm" not in file):
		if (file.endswith(".JPG")) or (file.endswith(".jpg")):
			fileName = file.split(".")
			picNames.append(fileName[0])
i = 0	
#iterate for each jpg file in the folder
while i < len(picNames):
	img = Image.open("./" + dirname + "/" + picNames[i] + ".JPG")
	new_width = 500
	new_height = 250
	img = img.resize((new_width, new_height), Image.ANTIALIAS)
	img.save("./" + dirname + "/" + picNames[i] + "_sm.JPG")
	img.close()
	i = i + 1