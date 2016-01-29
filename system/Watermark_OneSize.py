#!/usr/bin/python
import os
import time

def watermarkImage(latitude, longitude): 
	


	#Add company logo watermark 
	os.system("composite -dissolve  50% -gravity south Watermark.jpg scan_150dpi.jpg tempRotated.jpg")

	#Add text on side 
	arg = "convert canvas: tempRotated.jpg -gravity east -fill white -draw \"rectangle 0,0 100, 2000\" -rotate -270 \
			-gravity north -fill red -pointsize 20  -annotate +0+10 'Latitude: %d Longitude: %d' \
						   -annotate +0+35 'Time: %s' \
						   -annotate +0+60 'Project: Beta Prototype Example' -rotate 270 FinalImage.jpg" %(latitude, longitude, time.ctime())
	os.system(arg)
	os.system("rm tempRotated.jpg ")





          







