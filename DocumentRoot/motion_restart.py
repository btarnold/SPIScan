#!/usr/bin/python2.7
## Restart the motion daemon

from subprocess import call

call(["/etc/init.d/motion", "restart"])

