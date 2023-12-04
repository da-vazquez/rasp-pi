import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

trigPin = 23
echoPin = 24

def echoConversionToInch(travelTime):
	oneInch = 154
	distanceInch = int(travelTime / oneInch)
	distanceFoot = int(distanceInch / 12)
	print(f"Distance: {distanceInch} inches, {distanceFoot} feet")

GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

try:
	while True:
		GPIO.output(trigPin, 0)
		time.sleep(2E-6)
		GPIO.output(trigPin, 1)
		time.sleep(10E-6)
		GPIO.output(trigPin, 0)

		while GPIO.input(echoPin) == 0:
			pass
		echoStartTime = time.time() # grab echo time when high

		while GPIO.input(echoPin) == 1:
			pass

		echoStopTime = time.time() # grab echo time when low
		pingTravelTime = echoStopTime - echoStartTime

		# formattedPingTravelTime = (int(pingTravelTime * 1E6)) # multiply for 1 million
		# print(formattedPingTravelTime)
		# echoConversionToInch(formattedPingTravelTime) # Created a helper func to convert to inch

		distance = 767 * pingTravelTime * 5280 * 12 / 3600
		dtt = distance / 2 # distance is ping to target AND back so divide by 2
		print(round(dtt, 1), " inches")

		time.sleep(0.2)

except KeyboardInterrupt:
	GPIO.cleanup()
	print("GPIO pins cleared.")
