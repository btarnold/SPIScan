#!/usr/bin/env python

import sys
import json
import cgi
import os

fs = cgi.FieldStorage()

sys.stdout.write("Content-Type: application/json")

sys.stdout.write("\n")
sys.stdout.write("\n")

result = {}
result['success'] = True
result['message'] = "Called acquire_preview.py"
result['keys'] = ",".join(fs.keys())

d = {}
for k in fs.keys():
    d[k] = fs.getvalue(k)

result['data'] = d

scan_type = fs.getvalue('type')
if scan_type == 'preview':
    sys_call = 'python scanning/loscan.py'
elif scan_type == 'acquire':
    sys_call = 'python scanning/prescan.py'

#os.system(sys_call)


result['sys_call'] = sys_call
sys.stdout.write(json.dumps(result,indent=1))
sys.stdout.write("\n")
sys.stdout.close()
