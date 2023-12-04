import RPi.GPIO as GPIO
import ADC0834
from time import sleep

dt = 0.1
redPin = 23
DC = 0 # LED off duty cycle

GPIO.setmode(GPIO.BCM)

ADC0834.setup() # potentiometer turn on
GPIO.setup(redPin, GPIO.OUT) # LED pin

myPWM = GPIO.PWM(redPin, 1000) # htz
myPWM.start(DC)

try:
	while True:
		potVal = ADC0834.getResult(0)
		DC = (100 /255) * potVal
		if DC > 99:
			DC = 99
		myPWM.ChangeDutyCycle(DC)
		print(potVal, DC)
		sleep(dt)


except KeyboardInterrupt:
	myPWM.stop()
	GPIO.cleanup()
	print("cleaning up pins...")



