#!/usr/bin/env python

import sys
import json
import cgi,cgitb
import sqlite3
cgitb.enable()
fs = cgi.FieldStorage()

sys.stdout.write("Content-Type: application/json")

sys.stdout.write("\n")
sys.stdout.write("\n")


result = {}
result['success'] = True
result['message'] = "Jon == Brandon"
result['keys'] = ",".join(fs.keys())
docRoot = '/var/www/html/'
d = {}
for k in fs.keys():
    d[k] = fs.getvalue(k)

result['data'] = d

sys.stdout.write(json.dumps(result,indent=1))
sys.stdout.write("\n")
sys.stdout.close()

# Get data from fields

conn = sqlite3.connect(docRoot+'db/test.db')
id = fs.getvalue('id')
conn.execute("DELETE from SCANS where ID = "+id)
conn.commit()
conn.close()
'''print "Total number of rows updated :", conn.total_changes

cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
for row in cursor:
   print "ID = ", row[0]
   print "NAME = ", row[1]
   print "ADDRESS = ", row[2]
   print "SALARY = ", row[3], "\n"

print "Operation done successfully";'''
