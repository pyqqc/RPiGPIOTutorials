# Python Code to communicate with MCP3004

#Import SpiDev wrapper
import spidev
import time

#Establish SPI Connection on Bus 0, Device 0
spi = spidev.SpiDev()
spi.open(0,0)

DEBUG = True

def get_adc(channel):
    #Check Valid Channel
    if((channel > 3) or (channel < 0)):
        return -1
    #Transfer and filter data bits out from returned data
    r = spi.xfer([1, (8+channel)<<4, 0])
    adcout = ((r[1]&3) << 8) + r[2]
    percent = int(round(adcout/10.24))
    if(DEBUG):
        print adcout
        time.sleep(0.1)
    else:
        print("ADC Readout: {0} Percentage {1}".format(adcout,percent))

while True:
    get_adc(0)
