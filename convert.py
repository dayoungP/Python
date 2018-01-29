#Version 5/23/17 4:13PM
#Read "convert_notes.txt" for more information about this script
import os;
from time import strftime;
#get the directory name
dirname = raw_input('directory:\t')
#get the list of jpg file names
picNames = []
for file in os.listdir(r'{0}'.format(dirname)):
	if (file.endswith(".JPG")) or (file.endswith(".jpg")):
		if ("_sm" not in file):
			#don't include smaller jpg files
			fileName = file.split(".")
			picNames.append(fileName[0])
		
ofile = open("NewSphere.x3d", "r")
#load all lines from the original script and store them as a list
original = ofile.readlines()
i = 0
#iterate for each jpg file in the folder
while i < len(picNames): 
	#reset data to the original data lines
	data = list(original)
	#get current date and time
	timeInfo = strftime("%m/%d/%Y|%H:%M:%S")
	info = timeInfo.split("|")
	#iterate through data to replace header info and urls
	j = 0
	while j < len(data):
		if "ExportTime" in data[j]:
			data[j] = " <meta name=\'ExportTime\' content=\'" + info[1] + "\'/>\n"
		elif "ExportDate" in data[j]:
			data[j] = " <meta name=\'ExportDate\' content=\'" + info[0] + "\'/>\n"
		elif ("url=" in data[j]) and ("_sm" in data[j]):
			#case for smaller version of the file
			data[j] = "\t\turl=\'\"" + picNames[i] + "_sm.JPG" + "\"\'/>\n"
		elif ("url=" in data[j]) and ("_sm" not in data[j]):
			#case for original version
			data[j] = "\t\turl=\'\"" + picNames[i] + ".JPG" + "\"\'/>\n" 
		j = j + 1	
		
	#Create a new file that includes the name of jpg file that will be converted
	filename = "NewSphere_" + dirname + "_" + picNames[i] + ".x3d"
	newFile = open(dirname + "/" + filename, "w")
	#write the modified data
	newFile.writelines(data)
	newFile.close()
	i = i + 1
ofile.close()

