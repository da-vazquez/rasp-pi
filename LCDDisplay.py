import LCD1602
import time
LCD1602.init(0x27, 1)

try:
	while True:
		LCD1602.write(0, 0, "Hello World")
		LCD1602.write(0, 1, "Welcome!")

except KeyboardInterrupt:
	time.sleep(0.1)
	LCD1602.clear()
	print("LCD cleared.")
