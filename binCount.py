## IMPORTS
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

## DECLARE VARIABLES
LED1 = 37
LED2 = 35
LED3 = 33
LED4 = 31
LED5 = 29

sleep_time = 1

## GPIO SETUP
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(LED4, GPIO.OUT)
GPIO.setup(LED5, GPIO.OUT)

GPIO.output(LED1, 0)
GPIO.output(LED2, 0)
GPIO.output(LED3, 0)
GPIO.output(LED4, 0)
GPIO.output(LED5, 0)

## LET HANG
time.sleep(.5)

print(1)
GPIO.output(LED1, 1)
GPIO.output(LED2, 0)
GPIO.output(LED3, 0)
GPIO.output(LED4, 0)
GPIO.output(LED5, 0)
time.sleep(sleep_time)

print(2)
GPIO.output(LED1, 0)
GPIO.output(LED2, 1)
GPIO.output(LED3, 0)
GPIO.output(LED4, 0)
GPIO.output(LED5, 0)
time.sleep(sleep_time)

print(3)
GPIO.output(LED1, 0)
GPIO.output(LED2, 1)
GPIO.output(LED3, 0)
GPIO.output(LED4, 0)
GPIO.output(LED5, 0)
time.sleep(sleep_time)

print(4)
GPIO.output(LED1, 1)
GPIO.output(LED2, 1)
GPIO.output(LED3, 0)
GPIO.output(LED4, 0)
GPIO.output(LED5, 0)
time.sleep(sleep_time)

print(5)
GPIO.output(LED1, 0)
GPIO.output(LED2, 0)
GPIO.output(LED3, 1)
GPIO.output(LED4, 0)
GPIO.output(LED5, 0)
time.sleep(sleep_time)

print(6)
GPIO.output(LED1, 1)
GPIO.output(LED2, 0)
GPIO.output(LED3, 1)
GPIO.output(LED4, 0)
GPIO.output(LED5, 0)
time.sleep(sleep_time)

print(7)
GPIO.output(LED1, 0)
GPIO.output(LED2, 1)
GPIO.output(LED3, 1)
GPIO.output(LED4, 0)
GPIO.output(LED5, 0)
time.sleep(sleep_time)

print(8)
GPIO.output(LED1, 1)
GPIO.output(LED2, 1)
GPIO.output(LED3, 1)
GPIO.output(LED4, 0)
GPIO.output(LED5, 0)
time.sleep(sleep_time)

print(9)
GPIO.output(LED1, 0)
GPIO.output(LED2, 0)
GPIO.output(LED3, 0)
GPIO.output(LED4, 1)
GPIO.output(LED5, 0)
time.sleep(sleep_time)

print(10)
GPIO.output(LED1, 1)
GPIO.output(LED2, 0)
GPIO.output(LED3, 0)
GPIO.output(LED4, 1)
GPIO.output(LED5, 0)
time.sleep(sleep_time)

print(11)
GPIO.output(LED1, 0)
GPIO.output(LED2, 1)
GPIO.output(LED3, 0)
GPIO.output(LED4, 1)
GPIO.output(LED5, 0)
time.sleep(sleep_time)

print(12)
GPIO.output(LED1, 1)
GPIO.output(LED2, 1)
GPIO.output(LED3, 0)
GPIO.output(LED4, 1)
GPIO.output(LED5, 0)
time.sleep(sleep_time)

print(13)
GPIO.output(LED1, 0)
GPIO.output(LED2, 0)
GPIO.output(LED3, 1)
GPIO.output(LED4, 1)
GPIO.output(LED5, 0)
time.sleep(sleep_time)

print(14)
GPIO.output(LED1, 1)
GPIO.output(LED2, 0)
GPIO.output(LED3, 1)
GPIO.output(LED4, 1)
GPIO.output(LED5, 0)
time.sleep(sleep_time)

print(15)
GPIO.output(LED1, 0)
GPIO.output(LED2, 1)
GPIO.output(LED3, 1)
GPIO.output(LED4, 1)
GPIO.output(LED5, 0)
time.sleep(sleep_time)

print(16)
GPIO.output(LED1, 1)
GPIO.output(LED2, 1)
GPIO.output(LED3, 1)
GPIO.output(LED4, 1)
GPIO.output(LED5, 0)
time.sleep(sleep_time)

print(17)
GPIO.output(LED1, 0)
GPIO.output(LED2, 0)
GPIO.output(LED3, 0)
GPIO.output(LED4, 0)
GPIO.output(LED5, 1)
time.sleep(sleep_time)

print(18)
GPIO.output(LED1, 1)
GPIO.output(LED2, 0)
GPIO.output(LED3, 0)
GPIO.output(LED4, 0)
GPIO.output(LED5, 1)
time.sleep(sleep_time)

print(19)
GPIO.output(LED1, 0)
GPIO.output(LED2, 1)
GPIO.output(LED3, 0)
GPIO.output(LED4, 0)
GPIO.output(LED5, 1)
time.sleep(sleep_time)

print(20)
GPIO.output(LED1, 1)
GPIO.output(LED2, 1)
GPIO.output(LED3, 0)
GPIO.output(LED4, 0)
GPIO.output(LED5, 1)
time.sleep(sleep_time)

print(21)
GPIO.output(LED1, 0)
GPIO.output(LED2, 0)
GPIO.output(LED3, 1)
GPIO.output(LED4, 0)
GPIO.output(LED5, 1)
time.sleep(sleep_time)

print(22)
GPIO.output(LED1, 1)
GPIO.output(LED2, 0)
GPIO.output(LED3, 1)
GPIO.output(LED4, 0)
GPIO.output(LED5, 1)
time.sleep(sleep_time)

print(23)
GPIO.output(LED1, 0)
GPIO.output(LED2, 1)
GPIO.output(LED3, 1)
GPIO.output(LED4, 0)
GPIO.output(LED5, 1)
time.sleep(sleep_time)

print(24)
GPIO.output(LED1, 1)
GPIO.output(LED2, 1)
GPIO.output(LED3, 1)
GPIO.output(LED4, 0)
GPIO.output(LED5, 1)
time.sleep(sleep_time)

print(25)
GPIO.output(LED1, 0)
GPIO.output(LED2, 0)
GPIO.output(LED3, 0)
GPIO.output(LED4, 1)
GPIO.output(LED5, 1)
time.sleep(sleep_time)

print(26)
GPIO.output(LED1, 1)
GPIO.output(LED2, 0)
GPIO.output(LED3, 0)
GPIO.output(LED4, 1)
GPIO.output(LED5, 1)
time.sleep(sleep_time)

print(27)
GPIO.output(LED1, 0)
GPIO.output(LED2, 1)
GPIO.output(LED3, 0)
GPIO.output(LED4, 1)
GPIO.output(LED5, 1)
time.sleep(sleep_time)

print(28)
GPIO.output(LED1, 1)
GPIO.output(LED2, 1)
GPIO.output(LED3, 0)
GPIO.output(LED4, 1)
GPIO.output(LED5, 1)
time.sleep(sleep_time)

print(29)
GPIO.output(LED1, 0)
GPIO.output(LED2, 0)
GPIO.output(LED3, 1)
GPIO.output(LED4, 1)
GPIO.output(LED5, 1)
time.sleep(sleep_time)

print(30)
GPIO.output(LED1, 1)
GPIO.output(LED2, 0)
GPIO.output(LED3, 1)
GPIO.output(LED4, 1)
GPIO.output(LED5, 1)
time.sleep(sleep_time)

print(31)
GPIO.output(LED1, 0)
GPIO.output(LED2, 1)
GPIO.output(LED3, 1)
GPIO.output(LED4, 1)
GPIO.output(LED5, 1)
time.sleep(sleep_time)

print(32)
GPIO.output(LED1, 1)
GPIO.output(LED2, 1)
GPIO.output(LED3, 1)
GPIO.output(LED4, 1)
GPIO.output(LED5, 1)
time.sleep(sleep_time)

## CLEANUP
print("cleaning up GPIO pins...")
GPIO.cleanup()