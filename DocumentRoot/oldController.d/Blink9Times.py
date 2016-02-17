#!/usr/bin/python

import serial
import time
import sys
import json
import cgi

#ser = serial.Serial('/dev/ttyACM0', 115200) # open first serial port     		# check which port was really used
#time.sleep(2)
#ser.write('9')                      #write string
#time.sleep(2)
#ser.close()             	    # close port

fs = cgi.FieldStorage()

sys.stdout.write("Content-Type: application/json")

sys.stdout.write("\n")
sys.stdout.write("\n")


result = {}
result['success'] = True
result['message'] = "Jon == Brandon"
result['keys'] = ",".join(fs.keys())

d = {}
for k in fs.keys():
    d[k] = fs.getvalue(k)

result['data'] = d

sys.stdout.write(json.dumps(result,indent=1))
sys.stdout.write("\n")

sys.stdout.close()
