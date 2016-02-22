#!/usr/bin/python2.7
## Start the motion daemon

from subprocess import call

call(["/etc/init.d/motion", "start"])

