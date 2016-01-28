## This dynscan.py script is meant to be called like so:
##	dynscan.py dpi_number jpg_filename tiff_filename description
## Including a description is not strictly required.
## The use of file names is obsolete as of Tuesday, 26 Jan. 2016 when Brandon
##  reverted scan_start() in scan.c to take only one parameter again.

import dspace
import time
import sys

done = 0

num_args = len(sys.argv)
args = sys.argv

scan_array_pos = 1 # default to one -> the preview scan setting
if num_args>1:
	dpi_number=int(args[1])
else:
	dpi_number=0
if num_args>2:
	jpg_filename=args[2]
else:
	jpg_filename="/tmp/temp_scan.jpg"
if num_args>3:
	tiff_filename=args[3]
else:
	tiff_filename="/tmp/temp_scan.tiff"

## Set the description of the scan; no changes yet made to dspace.scan_description
#if num_args<4:
#	print( "Error, insufficient arguments" )
if num_args<=4:
	dspace.scan_description("test description");
else:
	dspace.scan_description(args[4])

## Set the position in the SCAN_TYPE array defined in scan.c that dspace.scan_start will use
#if (dpi_number==75 and description=="placement check"):
#	scan_array_pos=0
if dpi_number==75:
	scan_array_pos=1
elif dpi_number==100:
	scan_array_pos=2
elif dpi_number==150:
	scan_array_pos=3
elif dpi_number==200:
	scan_array_pos=4
elif dpi_number==300:
	scan_array_pos=5
elif dpi_number==600:
	scan_array_pos=6
elif dpi_number==1200:
	scan_array_pos=7
elif dpi_number==2400:
	scan_array_pos=8
elif dpi_number==4800:
	scan_array_pos=9

print ("Scan array position: ", scan_array_pos)
print ("\nDPI_number: ", dpi_number)

## Do the actual referencing of the C functions
while done==0:
	dspace.scan_start(scan_array_pos);
	while dspace.scan_done()==0:
		time.sleep(1)
	print ("scan done")
	done=1

