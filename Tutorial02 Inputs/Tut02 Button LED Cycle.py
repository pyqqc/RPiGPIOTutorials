import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()
ledPins = [16, 15, 29]
buttonPin = 12

for a in ledPins:
    GPIO.setup(a, GPIO.OUT)

GPIO.setup(buttonPin, GPIO.IN)

currentLed = 0

#while True:
 #   for a in ledPins:
  #      GPIO.output(a, True)
   # sleep(2)
    #for a in ledPins:
     #   GPIO.output(a, False)
    #sleep(2)

while True:
    pin = ledPins[currentLed]
    GPIO.output(pin, True)
    buttonIn = not GPIO.input(buttonPin)
    print(buttonIn)
    if buttonIn == True:
        GPIO.output(pin, False)
        if currentLed == 2:
            currentLed = 0
        else:
            currentLed = currentLed + 1
        sleep(0.1)
