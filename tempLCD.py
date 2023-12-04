import LCD1602
import RPi.GPIO as GPIO
import dht11
import time

GPIO.setmode(GPIO.BCM)
myDHT = dht11.DHT11(pin = 17)
LCD1602.init(0x27, 1)
buttonPin = 21
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

buttonState = 1
buttonStateOld = 1
tempMode = True


print("Reading Temperature!")
LCD1602.write(0,0, "Hello Dan!")
LCD1602.write(0,1, "Loading...")
time.sleep(2)


try:
	while True:
		buttonState = GPIO.input(buttonPin)
		if buttonState == 1 and buttonStateOld == 0:
			tempMode = not tempMode
		# print(tempMode)
		buttonStateOld = buttonState

		result = myDHT.read()
		tempC = result.temperature
		tempF = tempC * 1.8 + 32
		hum = result.humidity
		if result.is_valid():
			if tempMode == True:
				LCD1602.write(0,0, 'Temp: ')
				LCD1602.write(6,0, str(round(tempF,1)))
				LCD1602.write(10,0, 'F')
				LCD1602.write(0,1, 'Humidity: ')
				LCD1602.write(10,1, str(hum))
				LCD1602.write(14,1, '%')
			if tempMode == False:
                                LCD1602.write(0,0,"Temp: ")
                                LCD1602.write(6,0,str(round(tempC,1)))
                                LCD1602.write(10,0, "C")
                                LCD1602.write(0,1, "Humidity: ")
                                LCD1602.write(10,1, str(hum))
                                LCD1602.write(14,1, "%")
		# time.sleep(0.2)
except KeyboardInterrupt:
	LCD1602.clear()
	LCD1602.write(0,0,"Goodbye!")
	time.sleep(2)
	GPIO.cleanup()
	LCD1602.clear()
	print("GPIO and LCD cleared.")
