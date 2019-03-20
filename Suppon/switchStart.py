#!/usr/bin/python

#This script is to be run on startup of the device. It listens for the switch press which activates Scout Mode

import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def blink():
	for i in range(3):
		GPIO.output(17, True)
		time.sleep(.5)
		GPIO.output(17, False)
		time.sleep(.5)

def activate():
	blink()
	GPIO.output(17, True)

	print "[*] Activating Scout Mode"

	os.system("sudo ./checkPrev.sh")
	time.sleep(.2)

	print "[*] Starting monitor mode on wlan1" 
	os.system("sudo airmon-ng start wlan1")

	print "[*] Starting Kismet scan"
	os.system("kismet_server -c wlan1mon -t SUPPON -p kismetLogs --daemonize --no-line-wrap")

	while(True):
		if(GPIO.input(26) == False):
			print "[*] Stopping Kismet scan"
			GPIO.output(17, False)
			blink()
			os.system("sudo kill $(ps -aux | grep -m 1 kismet_server | awk -F' ' '{print $2}')")
			os.system("sudo airmon-ng stop wlan1mon")
			print "[*] Kismet scan ended"
			break

def main():
	try:
		while(True):
			if(GPIO.input(26) == False):
				activate()
				time.sleep(1)
				break
	except Exception as e:
		print "ERROR:"
		print e

if __name__ == "__main__":
	main()
