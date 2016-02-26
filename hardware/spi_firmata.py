#!/usr/bin/python

# led brightness 0-100 in increments of 10 controlled by pwm <==> PIN6
# pump1        <==>       PIN11
# pump2        <==>       PIN12
# lazer1       <==>       PIN2
# lazer2       <==>       PIN3
# lazer3       <==>       PIN4

# To get firmata onto the raspberry pi, run the following command:
# $ sudo apt-get install python-pip python-serial
# $ sudo pip install pyfirmata

from pyfirmata import Arduino, util
import time

def init():
	global board
	board = Arduino('/dev/ttyACM0')
	global lazer1
	lazer1 = board.get_pin('d:2:o')
	global lazer2
	lazer2 = board.get_pin('d:3:o')
	global lazer3
	lazer3 = board.get_pin('d:4:o')
	global pump1
	pump1 = board.get_pin('d:11:o')
	global pump2
	pump2 = board.get_pin('d:12:o')
	global pwm_led
	pwm_led = board.get_pin('d:6:p')

# Turn on all of the lazers
def lazers_toggle(input=-1):
	if(input < 0):
		cur = lazer1.read()
	else:
		cur = 1 - input
	if cur == 0:
		lazer1.write(1)
		lazer2.write(1)
		lazer3.write(1)
	else:
		lazer1.write(0)
		lazer2.write(0)
		lazer3.write(0)

# Toggle pump1
def pump1_toggle(input=-1):
	if(input < 0):
		cur = pump1.read()
	else:
		cur = 1 - input

	if cur == 0:
		pump1.write(1)
	else:
		pump1.write(0)

# Toggle pump2
def pump2_toggle(input=-1):
	if(input < 0):
		cur = pump2.read()
	else:
		cur = 1 - input

	if cur == 0:
		pump2.write(1)
	else:
		pump2.write(0)

# Turn on the pwm_led with the given Duty Cycle
def pwmLED(duty_cycle):
	pwm_led.write(duty_cycle * 0.01)
