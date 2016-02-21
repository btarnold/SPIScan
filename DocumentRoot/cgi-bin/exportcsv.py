#!/usr/bin/python
import os
import time
import sys
import json
import cgi

fs = cgi.FieldStorage()

sys.stdout.write("Content-Type: application/json")

sys.stdout.write("\n")
sys.stdout.write("\n")


result = {}
result['success'] = True
result['message'] = "Called exportcsv.py"
result['keys'] = ",".join(fs.keys())

d = {}
for k in fs.keys():
    d[k] = fs.getvalue(k)

result['data'] = d

#Resize Watermark resize to 3531
os.system('sqlite3 -header -csv /var/www/html/db/test.db "select * from SCANS;" > /var/www/html/db/test.csv')
os.system('zip -j /var/www/html/db.zip /var/www/html/db/test.csv /var/www/html/images/*')

sys.stdout.write(json.dumps(result,indent=1))
sys.stdout.write("\n")

sys.stdout.close()
