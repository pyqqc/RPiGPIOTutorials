import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
buttonPin = 23
GPIO.setup(buttonPin, GPIO.IN)

while True:
    buttonState = not GPIO.input(buttonPin)
    if buttonState:
        print("Button Pressed")
    else:
        print("Button Depressed")
    sleep(0.1)
