'''
Turn on LED when user presses button
Pull Up Resistor
Button hasn't been pushed? Returns a 1 since connects to 3.3v 
Button pushed? Returns a 0 since connects to ground
'''


## IMPORTS
from time import sleep
import RPi.GPIO as GPIO

'''
Set Pin Mode
'''

GPIO.setmode(GPIO.BOARD)

'''
Variables
'''

delay = 0.1
inPin = 40
outPin = 38

'''
Setup input and output pins
'''

GPIO.setup(inPin, GPIO.IN)
GPIO.setup(outPin, GPIO.OUT)

'''
Read values from input and activate output based on status
'''

try:
	while True:
		readVal = GPIO.input(inPin)
		# Check if button has NOT been pushed
		if readVal == 1:
			GPIO.output(outPin, 0)

		# Check if button has been pushed
		if readVal == 0:
			GPIO.output(outPin, 1)

except:
	## Cleanup Pins after gracefully exiting
	GPIO.cleanup()
	print("cleaning up GPIO pins...")

