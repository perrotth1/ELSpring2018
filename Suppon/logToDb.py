#!/usr/bin/python

import os
import glob
import sqlite3 as mydb

def writeDb(logStr):
	os.system("sudo touch kismetLogs/SUPPON.db")
	os.system("sudo chmod 755 kismetLogs/SUPPON.db")
	con = mydb.connect("kismetLogs/SUPPON.db")
	cur = con.cursor()
	cur.execute("CREATE TABLE networks(bssid TEXT, ssid TEXT, packets INTEGER, model TEXT, crypt TEXT, channel INTEGER, lat REAL, long REAL, alt REAL)")

	i = 0
	bssid = ""
	ssid = ""
	packets = 0
	model = ""
	crypt = ""
	channel = 0
	lat = ""
	long = ""
	alt = ""

	while(True):
		netSt = logStr.find("Network ", i)	#Get boundries of one network log
		netEn = logStr.find("wlan1mon", netSt)
		if(netSt == -1): break

		bssidSt = logStr.find("BSSID ", netSt, netEn)		#Grab BSSID
		bssidSt += 6
		bssid = logStr[bssidSt:bssidSt+17]

		ssidC = logStr.find("  SSID  ", bssidSt, netEn)
		if(ssidC == -1):
			i = netEn
			continue
		else:
			ssidSt = logStr.find(": ", ssidC, netEn)
			ssidSt += 2
			ssid_ = logStr[ssidSt:logStr.find("\n", ssidSt)].replace('"','')
			ssid = ssid_.replace(' ','')

		packC = logStr.find("Packets", netSt, netEn)
		packSt = logStr.find(":", packC)
		packSt += 2
		packets = logStr[packSt:logStr.find("\n",packSt)]

		modelC = logStr.find("Model Name", netSt, netEn)
		if(modelC == -1):
			model = "Unknown"
		else:
			modelSt = logStr.find(":", modelC)
			modelSt += 2
			model = logStr[modelSt:logStr.find("\n", modelSt)]

		cryptC = logStr.find("Encryption", netSt, netEn)
		cryptSt = logStr.find(":", cryptC)
		cryptSt += 2
		crypt = logStr[cryptSt:logStr.find("\n",cryptSt)]

		channelC = logStr.find("Channel", netSt, netEn)
		channelSt = logStr.find(":", channelC)
		channelSt +=2
		channel = logStr[channelSt:logStr.find("\n",channelSt)]

		##FIND LATITUDE AND LONGITUDE##
		latC = logStr.find("AvgLat", netSt, netEn)
		if(latC == -1):lat = "Unknown"
		else:
			latC += 7
			lat = logStr[latC:logStr.find(" AvgLon", netSt, netEn)]

		longC = logStr.find("AvgLon", netSt, netEn)
		if(longC == -1):long = "Unknown"
		else:
			longC += 7
			long = logStr[longC:logStr.find(" AvgAlt", netSt, netEn)]

		altC = logStr.find("AvgAlt", netSt, netEn)
		altN = logStr.find("\n", altC, netEn)
		if(altC == -1):alt = "Unknown"
		else:
			altC +=  7
			alt = logStr[altC:altN]

		i = netEn

		print [bssid,ssid,packets,model,crypt,channel,lat,long,alt]

		cur.execute("INSERT INTO networks VALUES(?,?,?,?,?,?,?,?,?)", (bssid,ssid,packets,model,crypt,channel,lat,long,alt))
		con.commit()

def main():
	logPath = "kismetLogs/SUPPON*.nettxt"
	wildPath = glob.glob(logPath)

	try:
		with open(wildPath[0], "r") as f:
			logStr = f.read()

		writeDb(logStr)

	except Exception as e:
		print e

if __name__ == "__main__":
	main()
