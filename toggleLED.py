import RPi.GPIO as GPIO
from time import sleep

delay = 0.1
inPin = 40
outPin = 38
GPIO.setmode(GPIO.BOARD)

GPIO.setup(outPin, GPIO.OUT)
GPIO.setup(inPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

LEDstate = 0 # OFF
buttonState = 1
buttonStateOld = 1

try:
	while True:
		buttonState = GPIO.input(inPin)
		print(buttonState)
		if buttonState == 1 and buttonStateOld == 0: # up and last time down
			LEDstate = not LEDstate
			GPIO.output(outPin, LEDstate)

		buttonStateOld = buttonState
		sleep(delay)

except KeyboardInterrupt:
	GPIO.cleanup()
	print("...cleaning up GPIO pins...")
