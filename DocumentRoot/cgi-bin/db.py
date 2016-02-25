#!/usr/bin/python2.7

import os, sys
import json
import cgi,cgitb
import sqlite3

docRoot = '/var/www/'

# Get data from fields
def delete_entry(id):
    conn = sqlite3.connect(docRoot+'db/test.db')
    conn.execute("DELETE from SCANS where ID = "+id)
    conn.commit()
    conn.close()

def purge():
    conn = sqlite3.connect(docRoot+'db/test.db')
    conn.execute("DELETE from SCANS")
    os.system("rm "+docRoot+'/scans/*')
    conn.commit()
    conn.close()

def update(id, usernotes):
    conn = sqlite3.connect(docRoot+'db/test.db')
    conn.execute("UPDATE SCANS set USERNOTES = '"+usernotes+"' where ID = "+id)
    conn.commit()
    conn.close()

fs = cgi.FieldStorage()
action = fs.getvalue('action')
id = fs.getvalue('id')
usernotes = fs.getvalue('newContent')
sys.stdout.write("Content-Type: application/json")
sys.stdout.write("\n")
sys.stdout.write("\n")

result = {}
result['success'] = True
result['message'] = "Called db.py"
result['keys'] = ",".join(fs.keys())
d = {}
for k in fs.keys():
    d[k] = fs.getvalue(k)

result['data'] = d



if(action == 'purge'):
    purge()
elif(action == 'delete_entry'):
    delete_entry(id)
elif(action == 'update'):
    update(id, usernotes)

sys.stdout.write(json.dumps(result,indent=1))
sys.stdout.write("\n")
sys.stdout.close()