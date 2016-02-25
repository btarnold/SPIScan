#!/usr/bin/python2.7
from subprocess import call
import sys
import json
import cgi
import os

host = 'localhost'

## Restart the motion daemon
def restart():
    os.system("service motion restart > /dev/null")

## Start the motion daemon
def start():
    os.system("service motion start > /dev/null")

## Stop the motion daemon
def stop():
    os.system("service motion stop > /dev/null")

## Take screenshot of motion feed
def screenshot():
    os.system("curl "+host+":8080/0/action/snapshot > /dev/null")

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
result['success'] = True
result['message'] = "Called motion.py"
result['keys'] = ",".join(fs.keys())

d = {}
for k in fs.keys():
    d[k] = fs.getvalue(k)

result['data'] = d

action = fs.getvalue('action')
map[action]() #oooo spicy
sys.stdout.write(json.dumps(result,indent=1))
sys.stdout.write("\n")

sys.stdout.close()
