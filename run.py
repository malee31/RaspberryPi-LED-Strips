import time
import RPi.GPIO as GPIO

pins = [11, 13, 15]
pwm = [0, 0, 0]
freq = [5, 7, 9]

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
print("Start")

try:
	for pin in range(len(pins)):
		GPIO.setup(pins[pin], GPIO.OUT)
		pwm[pin] = GPIO.PWM(pins[pin], freq[pin])
		pwm[pin].start(1)
	while(True):
		time.sleep(1)
except:
	for pin in range(len(pins)):
		print(pin)
		print(pins[pin])
		pwm[pin].stop()
		GPIO.output(pins[pin], GPIO.LOW)
	print("End")
	GPIO.cleanup()
