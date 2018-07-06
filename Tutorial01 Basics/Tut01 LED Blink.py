import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)#G4N
GPIO.setup(29, GPIO.OUT)#G5Y
GPIO.setup(31, GPIO.OUT)#G6N
GPIO.setup(11, GPIO.OUT)#G17N
GPIO.setup(12, GPIO.OUT)#G18Y
GPIO.setup(13, GPIO.OUT)#G27N
GPIO.setup(15, GPIO.OUT)#G22Y
GPIO.setup(16, GPIO.OUT)#G23Y
GPIO.setup(18, GPIO.OUT)#G24N

while True:
    GPIO.output(7, True)
    GPIO.output(29, True)
    GPIO.output(31, True)
    GPIO.output(11, True)
    GPIO.output(12, True)
    GPIO.output(13, True)
    GPIO.output(15, True)
    GPIO.output(16, True)
    GPIO.output(18, True)
    sleep(2)
    GPIO.output(7, False)
    GPIO.output(29, False)
    GPIO.output(31, False)
    GPIO.output(11, False)
    GPIO.output(12, False)
    GPIO.output(13, False)
    GPIO.output(15, False)
    GPIO.output(16, False)
    GPIO.output(18, False)
    sleep(2)

