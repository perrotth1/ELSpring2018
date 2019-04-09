#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

def main():
	try:
		print("\n ---{{ SUPPON ATTACK MODE }}--- \n\n")
		BSSID = raw_input("[*] Enter BSSID of Target Network: ")
		print BSSID

		GPIO.output(4, True)
		time.sleep(2)
		GPIO.output(4, False)

	except Exception as e:
		print("Error:")
		print(e)
		GPIO.cleanup()

if __name__=="__main__":
	main()
