import RPi.GPIO as GPIO
from time import sleep

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

ledPins = [17,27,22]
buttonPin = 23

for a in ledPins:
    GPIO.setup(a, GPIO.OUT)

GPIO.setup(buttonPin, GPIO.IN)
currentLed = 0

while True:
    pin = ledPins[currentLed]
    GPIO.output(pin, True)
    buttonIn = not GPIO.input(buttonPin)
    print buttonIn
    if buttonIn == True:
        GPIO.output(pin, False)
        if currentLed == 2:
            currentLed = 0
        else:
            currentLed = currentLed + 1
        sleep(0.1)
