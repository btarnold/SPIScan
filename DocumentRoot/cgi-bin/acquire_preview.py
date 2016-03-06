#!/usr/bin/env python
#Smaller CGI script for the preview and acquire scan buttons to functions
import sys
import json
import cgi
import os
from subprocess import call

fs = cgi.FieldStorage()

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

scan_type = fs.getvalue('type')
result['message'] = "Called "+ scan_type
if scan_type == 'preview':
    sys_call = 'python scanning/loscan.py'
elif scan_type == 'acquire':
    sys_call = 'python scanning/prescan.py'

#call(sys_call, shell=True)


result['sys_call'] = sys_call
sys.stdout.write(json.dumps(result,indent=1))
sys.stdout.write("\n")
sys.stdout.close()
