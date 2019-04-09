#!/usr/bin/python

#This script is to be run on startup of the device. It listens for the switch press which activates Scout Mode

import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def blink():
	for i in range(3):
		GPIO.output(17, True)
		time.sleep(.5)
		GPIO.output(17, False)
		time.sleep(.5)
	return

def activate():
	blink()
	GPIO.output(17, True)

	print("[*] Activating Scout Mode")

	os.system("./checkPrev.sh")
	time.sleep(.5)

	print ("[*] Starting monitor mode on wlan1")
	os.system("sudo airmon-ng start wlan1")
	time.sleep(.5)

	print ("[*] Starting Kismet scan")
	os.system("kismet_server -c wlan1mon -t SUPPON -p kismetLogs --no-line-wrap --use-gpsd-gps &")
	return

def main():
	try:
		#time.sleep(20)		#Give the Pi some time to finish startup
		blink()
		while(True):
			state = GPIO.input(5)
			if(state == False):
				activate()
				time.sleep(1)
				break
		while(True):
			if(GPIO.input(5) == False):
				print ("[*] Stopping kismet scan")
				GPIO.output(17, False)
				blink()
				os.system("kill $(ps -aux | grep -m 1 kismet_server | awk -F' ' '{print $2}')")
				time.sleep(8)
				os.system("sudo airmon-ng stop wlan1mon")
				time.sleep(8)
				print ("[*] Converting logged data to SQL database")
				os.system("sudo ./logToDb.py")
				GPIO.cleanup()
				break
	except KeyboardInterrupt:
		print ("[!] KEYBOARD INTERRUPT")
		GPIO.cleanup()

if __name__ == "__main__":
	main()
