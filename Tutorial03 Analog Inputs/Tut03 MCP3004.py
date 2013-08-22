#! /usr/bin/env python

# Python Code to communicate with MCP3004

#Import SpiDev wrapper and Sleep function from time
import spidev
from time import sleep

#Establish SPI Connection on Bus 0, Device 0
spi = spidev.SpiDev()
spi.open(0,0)

def get_adc(channel):
    #Check valid channel
    if((channel > 3) or (channel < 0)):
        return -1

    #Perform SPI transaction and store returned bits in 'r'
    r = spi.xfer([1, (8+channel)<<4, 0])
    
    #Filter data bits from returned bits
    adcout = ((r[1]&3) << 8) + r[2]
    percent = int(round(adcout/10.24))
    
    #Print 0-1023 and percentage
    print("ADC Output: {0:4d}     Percentage: {1:3d}%".format(adcout,percent))
    sleep(0.1)
    
while True:
    get_adc(0)