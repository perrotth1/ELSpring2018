#!/usr/bin/python

import RPi.GPIO as GPIO
import os
import time

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17,GPIO.OUT)
blinkTime = 5

def readTemp():
	tempfile = open("/sys/bus/w1/devices/28-000006979949/w1_slave")
	tempfile_text = tempfile.read()
	currentTime = time.strftime('%x %X %Z')
	tempfile.close()
	tempC=float(tempfile_text.split("\n")[1].split("t=")[1])/1000
	tempF=tempC*9.0/5.0+32.0
	return [currentTime, tempC, tempF]

def blinkOnce(pin):
	GPIO.output(pin,True)
	time.sleep(.1)
	GPIO.output(pin,False)
	time.sleep(.1)

try:
	with open("../log/tempLog.csv", "a",) as log:
		while True:
			input_state = GPIO.input(26)
			if input_state == False:
				for i in range(blinkTime):
					blinkOnce(17)
				time.sleep(.2)
				data = readTemp()
				sData = str(data[2]) + "*F"
				print sData
				log.write("{0},{1}\n".format(time.strftime("%Y-%m-%d %H:%M:%S"),str(sData)))

except KeyboardInterrupt:
	#os.system('clear')
	print "Ya damn crook!"
	GPIO.cleanup()

