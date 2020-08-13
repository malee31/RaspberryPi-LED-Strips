import time, json
import RPi.GPIO as GPIO

with open("./pins.json") as configFile:
	config = json.load(configFile)
	pins = config["pins"]
	freq = config["frequency"]

pwm = [None] * 3

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
print("Start")

try:
	duty = 1;
	for pin in range(len(pins)):
		GPIO.setup(pins[pin], GPIO.OUT)
		pwm[pin] = GPIO.PWM(pins[pin], freq)
		pwm[pin].start(10)
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
