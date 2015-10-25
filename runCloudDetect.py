#!/usr/bin/env python2.7  
# script by Alex Eames http://RasPi.tv  
#http://RasPi.tv/2013/how-to-use-soft-pwm-in-rpi-gpio-pt-2-led-dimming-and-motor-speed-control  

  
import RPi.GPIO as GPIO # always needed with RPi.GPIO  
from time import sleep  # pull in the sleep function from time module  
from BMP085 import BMP085
from TMP007 import TMP007
import psycopg2
import picamera

camera = picamera.PiCamera()

conn = psycopg2.connect(host='frohmaierdb.c8d7umbjrqmj.us-west-2.rds.amazonaws.com', port=5432, user='cf5g09', password='SotonRoof2015!!', database='B46Roof')
cur=conn.cursor()
tmp=TMP007()
bmp=BMP085()

for i in range(0,5):

	print 'IR Temp: ', tmp.readObjTempC()
	print 'Die Temp: ', tmp.readDieTempC()
	print 'Voltage: ', tmp.readVoltage()
	print 'Amb Temp: ', bmp.read_temperature()
	print 'Pressure: ', bmp.read_pressure()
	print 'Altitude: ', bmp.read_altitude()
	cur.execute("INSERT INTO nightlog (ir_temp,amb_temp,pressure,die_temp,altitude,voltage) VALUES (%s,%s,%s,%s,%s,%s) RETURNING imageid;", (float(tmp.readObjTempC()),float(bmp.read_temperature()),float(bmp.read_pressure()),float(tmp.readDieTempC()),float(bmp.read_altitude()),float(tmp.readVoltage()),))
	ir_id=cur.fetchone()
	ir_id=int(ir_id[0])
	conn.commit()
	camera.capture('/home/pi/ir_clouds_pi/night_images/IR_Image_'+str(ir_id)+'.jpg')
	


	sleep(10)

	print '-----'