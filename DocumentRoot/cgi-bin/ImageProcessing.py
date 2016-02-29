#!/usr/bin/python
import os
import time
import subprocess


def watermarkImage(latitude, longitude, filename): 
	#Obtain Dimensions of image through system response 
	dimensions = getDimensions(filename)

	#Parse Length and Width of Image 
	length = getLength(dimensions)
	width = getWidth(dimensions)

	#print length + " " + width

	#Resize Watermark 
	resizeFactor = (width/float(700))*100
	argResize="convert Logo.jpg -resize %d"%(resizeFactor)

	os.system(argResize+"%"+" tempLogo.png")

	#Add company logo watermark 
	os.system("composite -dissolve  50% -gravity south tempLogo.png "+filename+" tempRotated.jpg")

	#Add text on side 
	arg = "convert canvas: tempRotated.jpg -gravity east -fill white -draw \"rectangle 0,0 30, %d\" -rotate -270 \
			-gravity north -fill red -pointsize 10  -annotate +0+3 'Latitude: %lf Longitude: %lf' \
						   -annotate +0+16 'Time: %s' \
						   -rotate 270 Image.tiff" %(length, latitude, longitude, time.ctime())
	os.system(arg)

	#Separate Image Array and Delete First Blank Entry 
	os.system("convert Image.tiff FinalImage%d.tiff" )
	os.system("rm Image.tiff FinalImage0.tiff")

	#Remove Temporary Files
	os.system("rm temp*")

	#Create World File 
	outputTWF(latitude, longitude, width, length)

	#Convert to geotiff
	arg = "geotifcp -e FinalImage1.tfw -p contig FinalImage1.tiff %s_GEO.tiff" %(filename.strip(".jpg"))
	os.system(arg)
	os.system("rm FinalImage*")

def outputTWF(latitude, longitude, width, length): 
	#xScale and yScale Refer to units per pixel 
	xScale = "0.00011559999999999991"
	yScale = "-0.00011559999999999991"

	outFile = open("FinalImage1.tfw", 'w')
	outFile.write(xScale+"\n"
				  +"0\n0\n"+yScale+"\n%lf\n%lf" %(latitude, longitude))

	outFile.close()

def getDimensions(filename): 
	p = subprocess.Popen(["identify "+filename], stdout=subprocess.PIPE, shell=True)
	OSout = p.stdout.read()
	return  OSout.split(" ")[2]

def getWidth(dim): 
	#Width comes first 
	return int(dim.split("x")[0])

def getLength(dim): 
	#Length comes second 
	return int(dim.split("x")[1])





