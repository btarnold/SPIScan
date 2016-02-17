#!/usr/bin/env python

import sys
import json
import cgi
import os
import sqlite3
import time
import spi_gps
import Watermark_OneSize

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

dpi = fs.getvalue('resolution')
user_notes = fs.getvalue('userNotes')

#get coordinates from GPS module

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
localtime = time.strftime('%Y-%m-%d_%H:%M:%S')
#print localtime

#construct filename
jpg_filename = localtime + '.jpg';
tiff_filename = localtime + '.tiff';
long = spi_gps.get_longitude()
lat =spi_gps.get_latitude()
location = "long:"+str(long)+" lat:"+str(lat)
if(not user_notes):
    user_notes = 'null'

query = "INSERT INTO SCANS (ID,FILENAME,DPI,USERNOTES,TIME,LOCATION) \
      VALUES ("+str(new_id)+", '"+jpg_filename+"',"+str(dpi)+", \
      '"+user_notes+"', '"+localtime+"','"+location+"' )"




image_dir = '/var/www/scans/'
sys_call = 'python scanning/dynscan.py '+str(dpi) + ' '+ jpg_filename
#if(user_notes)
#    sys_call += user_notes
os.system(sys_call)
os.system("ln -sf " + image_dir + jpg_filename +" "+image_dir+ "lastScan.jpg")


result['query'] = query
sys.stdout.write(json.dumps(result,indent=1))
sys.stdout.write("\n")
sys.stdout.close()
conn.execute(query)
conn.commit()
conn.close()

Watermark_OneSize.watermarkImage(longitude=long, latitude=lat, filename=image_dir+jpg_filename)
