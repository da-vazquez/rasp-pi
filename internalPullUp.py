import RPi.GPIO as GPIO
from time import sleep

delay = 0.1
inPin = 40
outPin = 38

GPIO.setmode(GPIO.BOARD)
GPIO.setup(outPin, GPIO.OUT)
GPIO.setup(inPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
	while True:
		readVal = GPIO.input(inPin)

		# button has not been pressed
		if readVal == 1:
			GPIO.output(outPin, 0)

		# button has been pressed
		if readVal == 0:
			print("button has been pressed!")
			GPIO.output(outPin, 1)

		sleep(delay)
except KeyboardInterrupt:
	GPIO.cleanup()
	print(" cleaning up GPIO pins...")

