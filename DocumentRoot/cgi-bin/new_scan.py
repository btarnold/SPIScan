#!/usr/bin/env python
#This CGI file creates a new scan, takes GPS + time, stores all information into database.

## IMPORTED LIBRARIES AND FUNCTIONS
import sys
import json
import cgi
import os
import sqlite3
import datetime
import df
from subprocess import call
#from shutil import copy2
#from ImageProcessing import watermarkImage
#import spi_gps

#prepare response
fs = cgi.FieldStorage()

sys.stdout.write("Content-Type: application/json")
sys.stdout.write("\n")
sys.stdout.write("\n")
result = {}
result['type'] = 'success'
result['message'] = "Scanned successfully"
result['keys'] = ",".join(fs.keys())

d = {}
for k in fs.keys():
    d[k] = fs.getvalue(k)
result['data'] = d

#get disk percentage and end if we are too full
percentage = int(df.disk_space().split('%')[0])
if(percentage >= 80 ):
    result['message'] = "Disk too full, please export and purge"
    result['type'] = 'danger'
    sys.stdout.write(json.dumps(result,indent=1))
    sys.stdout.write("\n")
    sys.exit()

#get field storage
dpi = int(fs.getvalue('resolution'))
user_notes = fs.getvalue('userNotes')
prefix = fs.getvalue('prefix')
ts_epoch = int(fs.getvalue('time'))/1000

#get coordinates from GPS module
gps_lat = 35.284932 #spi_gps.get_latitude() TODO: Uncomment and init GPS on startup
gps_long = -120.656834 #spi_gps.get_longitude()
gps_time = None #spi_gps.get_time()
if(gps_time and gps_time != 'N/A'):
    gps_time = gps_time.split('T').join('_').split('.')[0] #dear god....
gps_string = 'Lat: ' + str(gps_lat) + ' Long: '+ str(gps_long)
sys.stderr.write(gps_string+"\n") 
conn = sqlite3.connect('/var/www/db/test.db')

#compute new id by looking at the max id + 1 from sqlte DB
cursor = conn.execute("SELECT MAX(ID) FROM SCANS;")
for row in cursor:
    if(row[0]):
        new_id = int(row[0]) + 1
    else:
        new_id = 1
    break

#time
localtime = datetime.datetime.fromtimestamp(ts_epoch).strftime('%Y-%m-%d_%H:%M:%S')
used_time = gps_time if gps_time and gps_time != 'N/A' else localtime

#construct filename
jpg_filename = localtime + '.jpg';
tiff_filename = localtime + '.tiff';
if(prefix):
    jpg_filename = prefix +'_'+ jpg_filename
    tiff_filename = prefix +'_'+ tiff_filename

if(user_notes):
    user_notes = user_notes.replace("'","''") #fun sql apostrophe stuff
else:
    user_notes = 'null'



query = "INSERT INTO SCANS (ID,FILENAME,DPI,USERNOTES,TIME,LOCATION) \
      VALUES ("+str(new_id)+", '"+tiff_filename+"',"+str(dpi)+", \
      '"+user_notes+"', '"+used_time+"','"+gps_string+"' )"


## IMAGE FILE LOCATION MANIPULATION
#### Brandon removed uses of 'os.system' and replaced with calls to 'subprocess.call'
# image_dir = '/var/www/scans/'
# call(["python","scanning/dynscan.py",str(dpi),jpg_filename])
# jfn = image_dir+jpg_filename
# last = image_dir+"lastScan.jpg"
# call(["cp",jfn,last]) # Copy the image to lastScan.jpg as well. Would be better (less space) to do a symlink

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
#call('exiftool -GPSLongitude="'+str(gps_long)+'"  -GPSLatitude="'+str(gps_lat)+'" -GPSLatitudeRef="'+lat_ref+'" -GPSLongitudeRef="'+long_ref+'"  '+jpg_filename,shell=True)

sys.stdout.close()
conn.execute(query)
conn.commit()
conn.close()
