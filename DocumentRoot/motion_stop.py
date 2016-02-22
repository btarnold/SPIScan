#!/usr/bin/python2.7
## Stop the motion daemon

from subprocess import call

call(["/etc/init.d/motion", "stop"])

