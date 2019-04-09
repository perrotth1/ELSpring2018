import RPi.GPIO as GPIO
import time
import datetime
import sqlite3 as mydb

inPin = 22
outPin = 6

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(inPin, GPIO.IN)
GPIO.setup(outPin, GPIO.IN)
GPIO.setup(17, GPIO.OUT)

def main():
	con = mydb.connect("motionLog.db")		#Setting up database
	cur = con.cursor()

	cur.execute("DELETE FROM motions")

	occupants = 0
	now = ""

	print "[*] Stabilizing the sensors"
	time.sleep(20)

	print "[*] Starting detection"
	try:
		while(True):
			while(GPIO.input(outPin) == True):		#Person starts to enter. Outer sensor starts 5 second high state
				if(GPIO.input(inPin) == True):		#Person enters. Inner sensor starts 5 second high state
					print "[!] Someone has entered"
					occupants += 1
					now = str(datetime.datetime.now())[:-7]		#Get date and time, remove last decimal value of seconds
					cur.execute("INSERT INTO motions VALUES(?,?,?)", (now, "ENTRY", occupants))
					con.commit()
					GPIO.output(17, True)
					time.sleep(5)
					GPIO.output(17, False)
					while(GPIO.input(inPin) == True):	#In case someone wants to stand in the doorway like a vampire
						time.sleep(.1)

			while(GPIO.input(inPin) == True):		#Person starts to exit. Inner sensor starts 5 seconds high state
				if(GPIO.input(outPin) == True):		#Person exits. Outer sensor starts 5 seconds high state
					print "[!] Someone has left"
					occupants -= 1
					now = str(datetime.datetime.now())[:-7]
					cur.execute("INSERT INTO motions VALUES(?,?,?)", (now, "EXIT", occupants))
					con.commit()
					GPIO.output(17, True)
					time.sleep(5)
					GPIO.output(17, False)
					while(GPIO.input(outPin) == True):
						time.sleep(.1)
	except Exception as e:
		print e
		GPIO.cleanup()

if __name__ == "__main__":
	main()

