#!/usr/bin/env python

import sys
import json
import cgi
import os
import sqlite3
import time

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

dpi = int(fs.getvalue('resolution'))
user_notes = fs.getvalue('userNotes')

'''
image_directory = '/var/www/images';
sys_call = 'scanning/dynscan.py '+str(dpi)+' '+image_directory+jpeg_filename+' '+image_directory+tiff_filename
if(user_notes)
    sys_call += user_notes
os.system(sys_call)
'''
#get coordinates from GPS module

#connect to db and get picture number/var/www/images

conn = sqlite3.connect('/var/www/html/db/test.db')
#print "Opened database successfully"

#compute new id by looking at the max id + 1 from sqlte DB
cursor = conn.execute("SELECT MAX(ID) FROM SCANS;")
for row in cursor:
    new_id = int(row[0]) + 1
    break
#print new_id

#time
localtime = time.strftime('%Y-%m-%d_%H:%M:%S')
#print localtime

#construct filename
jpeg_filename = localtime + '.jpeg';
tiff_filename = localtime + '.tiff';

location = 'N/A'
if(not user_notes):
    user_notes = 'null'

query = "INSERT INTO SCANS (ID,FILENAME,DPI,USERNOTES,TIME,LOCATION) \
      VALUES ("+str(new_id)+", '"+jpeg_filename+"',"+str(dpi)+", \
      '"+user_notes+"', '"+localtime+"','"+location+"' )"
result['query'] = query
sys.stdout.write(json.dumps(result,indent=1))
sys.stdout.write("\n")

sys.stdout.close()
conn.execute(query)
conn.commit()
conn.close()
