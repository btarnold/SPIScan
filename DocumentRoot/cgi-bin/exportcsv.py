#!/usr/bin/python

#This CGI Script is for exporting the current database information into a csv file and then zipping it with contents of the /scans folder
import os
import time
import sys
import json
import cgi
from subprocess import call

fs = cgi.FieldStorage()

sys.stdout.write("Content-Type: application/json")

sys.stdout.write("\n")
sys.stdout.write("\n")


result = {}
result['type'] = 'success'
result['message'] = "Exported and Zipped"
result['keys'] = ",".join(fs.keys())


d = {}
for k in fs.keys():
    d[k] = fs.getvalue(k)

result['data'] = d

call('sqlite3 -header -csv /var/www/db/test.db "select * from SCANS;" > /var/www/db/test.csv', shell=True)
call('zip -j /var/www/db.zip /var/www/db/test.csv /var/www/scans/*', shell=True)

sys.stdout.write(json.dumps(result,indent=1))
sys.stdout.write("\n")

sys.stdout.close()
