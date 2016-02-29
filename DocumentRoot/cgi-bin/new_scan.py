#!/usr/bin/env python

## IMPORTED LIBRARIES AND FUNCTIONS
import sys
import json
import cgi
import os
import sqlite3
import datetime
import df
from subprocess import call
from shutil import copy2
from ImageProcessing import watermarkImage
#import spi_gps

fs = cgi.FieldStorage()

sys.stdout.write("Content-Type: application/json")

sys.stdout.write("\n")
sys.stdout.write("\n")


result = {}
result['success'] = True
result['message'] = "Called new_scan.py"
result['keys'] = ",".join(fs.keys())

d = {}
for k in fs.keys():
    d[k] = fs.getvalue(k)

result['data'] = d

percentage = int(df.disk_space().split('%')[0])
if(percentage > 75 ):
    result['success'] = False
    sys.stdout.write(json.dumps(result,indent=1))
    sys.stdout.write("\n")
    sys.exit()

dpi = int(fs.getvalue('resolution'))
user_notes = fs.getvalue('userNotes')
prefix = fs.getvalue('prefix')
ts_epoch = int(fs.getvalue('time'))/1000

#get coordinates from GPS module
gps_lat = 3.0 #spi_gps.get_latitude()
gps_long = 3.0 #spi_gps.get_longitude()
gps_string = str(gps_lat) + str(gps_long)
#connect to db and get picture number/var/www/images

conn = sqlite3.connect('/var/www/db/test.db')
#print "Opened database successfully"

#compute new id by looking at the max id + 1 from sqlte DB
cursor = conn.execute("SELECT MAX(ID) FROM SCANS;")
for row in cursor:
    if(row[0]):
        new_id = int(row[0]) + 1
    else:
        new_id = 1
    break
#print new_id

#time
localtime = datetime.datetime.fromtimestamp(ts_epoch).strftime('%Y-%m-%d_%H:%M:%S')
#print localtime

#construct filename
jpg_filename = localtime + '.jpg';
tiff_filename = localtime + '.tiff';

if(prefix):
    jpg_filename = prefix +'_'+ jpg_filename
    tiff_filename = prefix +'_'+ tiff_filename

location = 'N/A'
if(not user_notes):
    user_notes = 'null'

query = "INSERT INTO SCANS (ID,FILENAME,DPI,USERNOTES,TIME,LOCATION) \
      VALUES ("+str(new_id)+", '"+jpg_filename+"',"+str(dpi)+", \
      '"+user_notes+"', '"+localtime+"','"+gps_string+"' )"


## IMAGE FILE LOCATION MANIPULATION
#### Brandon removed uses of 'os.system' and replaced with calls to 'subprocess.call'
image_dir = '/var/www/scans/'
call(["python","scanning/dynscan.py",str(dpi),jpg_filename])
### sys_call = 'python scanning/dynscan.py '+str(dpi) + ' '+ jpg_filename
### os.system(sys_call)
### sys_call = 'cp '+image_dir+jpg_filename+' '+image_dir+'lastScan.jpg'
### sys_call = 'ln -s '+image_dir+jpg_filename+' '+image_dir+'lastScan.jpg'
### os.system(sys_call)
jfn = image_dir+jpg_filename
last = image_dir+"lastScan.jpg"
call(["rm", last])	# Remove the previous 'lastScan.jpg' file
call(["cp",jfn,last]) # Copy the image to lastScan.jpg as well. Would be better (less space) to do a symlink


result['query'] = query
sys.stdout.write(json.dumps(result,indent=1))
sys.stdout.write("\n")

#watermarkImage(gps_lat, gps_long, image_dir+jpg_filename)
if(gps_lat < 0):
    lat_ref = 'S'
else:
    lat_ref = 'N'
if(gps_long < 0):
    long_ref = 'W'
else:
    long_ref = 'E'
#os.system('exiftool -GPSLongitude="'+str(gps_long)+'"  -GPSLatitude="'+str(gps_lat)+'" -GPSLatitudeRef="'+lat_ref+'" -GPSLongitudeRef="'+long_ref+'"  '+jpg_filename)

sys.stdout.close()
conn.execute(query)
conn.commit()
conn.close()
