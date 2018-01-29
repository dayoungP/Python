#version 7/12/17
import os;
from subprocess import call
#get the directory name
directory = raw_input('directory:\t')
#get the list of x3d file names
x3dNames = []
for file in os.listdir(r'{0}'.format(directory)):
	if (file.endswith(".x3d")):
		#if ("_aopt" not in file):
			#don't include aopted files
			fileName = file.split(".")
			x3dNames.append(fileName[0])

i = 0

#while i < len(x3dNames):

#	os.system("aopt -i " + directory + "/" + x3dNames[i] + ".x3d -u -x " + directory + "/" + x3dNames[i] + "_aopt.x3d")
#	i = i + 1
	
	
while i < len(x3dNames):
	output = directory +"/"+ x3dNames[i] + "binGeo"
	os.system("mkdir " + output)
	os.system("aopt -i " + directory + "/" + x3dNames[i] + ".x3d -G " + output + "/:sacp -x " + directory + "/" + x3dNames[i] + "_bin.x3d")
	i = i + 1