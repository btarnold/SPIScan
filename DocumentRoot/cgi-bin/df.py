#!/usr/bin/python
#hacky file used to get disk space usage from the first entry of unix command df, (should be correct for RPi)
import sys
import subprocess

def disk_space():
    #get diskspace output
    output = subprocess.check_output('df')
    lines = output.split('\n')
    #get first line of disk space information
    main_line = lines[1]
    #get percentage used (in the 5th column)
    percentage = main_line.split()[4]
    return percentage
