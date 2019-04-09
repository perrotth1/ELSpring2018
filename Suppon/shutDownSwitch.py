#!/usr/bin/python

import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def main():
	try:
		while(True):
			input = GPIO.input(21)
			if(input == False):
				print "Low State"
				os.system("sudo halt -n")
				break
	except KeyboardInterrupt as e:
		print "KEYBOARD INTERRUPT"
		GPIO.cleanup()

if __name__ == "__main__":
	main()
