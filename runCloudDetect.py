#!/usr/bin/env python2.7  
# script by Alex Eames http://RasPi.tv  
#http://RasPi.tv/2013/how-to-use-soft-pwm-in-rpi-gpio-pt-2-led-dimming-and-motor-speed-control  

  
import RPi.GPIO as GPIO # always needed with RPi.GPIO  
from time import sleep  # pull in the sleep function from time module  
from BMP085 import BMP085
from TMP007 import TMP007

import sqlite3
conn = sqlite3.connect('ir_cloud.db')

tmp=TMP007()
bmp=BMP085()

for i in range(0,5):
	print 'IR Temp: ', tmp.readObjTempC()
	print 'Die Temp: ', tmp.readDieTempC()
	print 'Voltage: ', tmp.readVoltage()
	print 'Amb Temp: ', bmp.read_temperature()
	print 'Pressure: ', bmp.read_pressure()
	sleep(60)

print '-----'