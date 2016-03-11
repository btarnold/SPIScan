#!/usr/bin/python2.7
# This CGI Python script is invoked when any of the 
# webcam buttons on the deploy webpage is called.
# It directly calls any command line statements that
# are involved with motion.
from subprocess import call
import sys
import json
import cgi
import os

host = os.environ['REMOTE_ADDR']

## Restart the motion daemon
def restart():
    call("service motion restart", shell=True)

## Start the motion daemon
def start():
    call("service motion start", shell=True)

## Stop the motion daemon
def stop():
    call("service motion stop", shell=True)

## Take screenshot of motion feed
def screenshot():
    call("curl "+host+":8080/0/action/snapshot > /dev/null", shell=True)

map = {
    'restart':restart,
    'start':start,
    'stop':stop,
    'screenshot':screenshot
}

fs = cgi.FieldStorage()

sys.stdout.write("Content-Type: application/json")

sys.stdout.write("\n")
sys.stdout.write("\n")


result = {}
result['type'] = 'success'
result['keys'] = ",".join(fs.keys())
result['host'] = host

d = {}
for k in fs.keys():
    d[k] = fs.getvalue(k)

result['data'] = d

action = fs.getvalue('action')
result['message'] = "Called "+action
map[action]()
sys.stdout.write(json.dumps(result,indent=1))
sys.stdout.write("\n")

sys.stdout.close()
