	#!/usr/bin/python
import os
import time
import subprocess

def watermarkImage(latitude, longitude, time): 
	#Get Image Dimensions 

	p= subprocess.Popen(["identify", "ScannedImage.jpg"], stdout=subprocess.PIPE)
	imageDim= ''.join(p.communicate()[0]).split(' ')[2]
	width= int(imageDim.split('x')[0])
	length= int(imageDim.split('x')[1])

	#imageSize= imageProperties.rpartition('x')
	print imageDim
	print length 
	print width



		#Add company logo watermark 

		#os.system("identify ScannedImage.jpg")
		#systemResponse = sys.stdout.read()
		#print "from script: " + systemResponse

		#imageSize = str(systemResponse).split('x')
		#print imageSize

	

	#Resize Watermark!! 


		


	os.system("composite -dissolve  30% -gravity south Watermark.jpg scannedImage.JPG  temp.png")

	#Add text on side 
	arg = "convert canvas: temp.png -gravity east -fill white -draw \"rectangle 0,0 %d, %d\" -rotate -270  \
				-gravity north -fill red  -annotate +0+10 'Latitude: %d Longitude: %d' \
							   -annotate +0+25 'Time: %s' \
							  -annotate +0+40 'Project: Cat' -rotate 270 CatFinalMockUp.tiff" %(length, width*0.05, latitude, longitude, time)
	os.system(arg) 
		#os.system("rm *.png")





	          







