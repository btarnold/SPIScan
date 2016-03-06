#!/usr/bin/python2.7
#This CGI Script is for updating user notes, deleting single entries, or purging the database
import subprocess, sys
import json
import cgi,cgitb
import sqlite3
import glob, os

docRoot = '/var/www/'

# Get data from fields
def delete_entry(id):
    conn = sqlite3.connect(docRoot+'db/test.db')
    conn.execute("DELETE from SCANS where ID = "+id)
    conn.commit()
    conn.close()
    result['message'] = "Deleted entry"

def purge():
    conn = sqlite3.connect(docRoot+'db/test.db')
    conn.execute("DELETE from SCANS")
    for filename in glob.glob(docRoot+'scans/*'):
        os.remove(filename)
    if(os.path.isfile(docRoot+'db.zip')): #scared about this check.. you should only purge if you've zipped....
        os.remove(docRoot+'db.zip')
    conn.commit()
    conn.close()
    result['message'] = "Purged database"

def update(id, usernotes):
    conn = sqlite3.connect(docRoot+'db/test.db')
    conn.execute("UPDATE SCANS set USERNOTES = '"+usernotes+"' where ID = "+id)
    conn.commit()
    conn.close()
    result['message'] = "Updated usernotes"

fs = cgi.FieldStorage()
action = fs.getvalue('action')
id = fs.getvalue('id')
usernotes = fs.getvalue('newContent')
sys.stdout.write("Content-Type: application/json")
sys.stdout.write("\n")
sys.stdout.write("\n")

result = {}
result['type'] = 'success'

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