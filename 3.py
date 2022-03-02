import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.OUT)
GPIO.setup(14, GPIO.IN)

while True:
    GPIO.output(26, GPIO.input(14))
