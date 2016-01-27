#!/usr/bin/python
import os
import time

def watermarkImage(latitude, longitude, time): 
	
	#Resize Watermark resize to 3531 
	os.system("convert Watermark.jpg -resize 400% resizedWatermark.png")

	#Add company logo watermark 
	os.system("composite -dissolve  20% -gravity south resizedWatermark.png scan.jpg tempRotated.png")

	#Add text on side 
	arg = "convert canvas: tempRotated.png -gravity east -fill white -draw \"rectangle 0,0 200, 20000\" -rotate -270 \
			-gravity north -fill red -pointsize 60  -annotate +0+10 'Latitude: %d Longitude: %d' \
						   -annotate +0+75 'Time: %s' \
						   -annotate +0+130 'Project: Beta Prototype Example' -rotate 270 FinalImage.tiff" %(latitude, longitude, time)
	os.system(arg)
	os.system("rm tempRotated.png ")





          







