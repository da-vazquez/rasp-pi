import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(38, GPIO.OUT)


try:
	while True:
		GPIO.output(38, True)
		#myPMW = GPIO.PWM(38, 100)
		#myPMW.start(50)

except KeyboardInterrupt:
	GPIO.cleanup()
	print("cleaning up GPIO pins...")
