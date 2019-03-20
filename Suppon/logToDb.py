#!/usr/bin/python

import os
import glob
import sqlite3 as mydb

logStr = ""

def writeDb():
	os.system("sudo touch kismetLogs/SUPPON.db")
	os.system("sudo chmod 755 kismetLogs/SUPPON.db")
	con = mydb.connect("kismetLogs/SUPPON.db")
	cur = con.cursor()
	cur.execute("CREATE TABLE networks(ssid TEXT, crypt TEXT, channel INTEGER, bssid TEXT, packets INTEGER, lat REAL, long REAL)")


def main():
	logPath = "kismetLogs/SUPPON*.nettxt"
	wildPath = glob.glob(logPath)

	try:
		with open(wildPath[0], "r") as f:
			logStr = f.read()
		writeDb()

	except Exception as e:
		print e

if __name__ == "__main__":
	main()
