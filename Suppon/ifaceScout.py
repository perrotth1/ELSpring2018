#!/usr/bin/python

from flask import Flask
from flask import render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
import sqlite3 as db

app = Flask(__name__)

GoogleMaps(app,key="AIzaSyD7QYBX87SaTCa6gU3bTkSK_Z2GHfcfgk0")

con = db.connect("kismetLogs/SUPPON.db")
cur = con.cursor()
netData = [[],[],[],[],[],[],[],[],[]]

with con:
	try:
		for row in cur.execute("SELECT * FROM networks"):
			for x in range(9):
				netData[x].append(row[x])
	except Exception as e:
		print(e)

netMarkers = []
for i in range(len(netData[0])):
	netMarkers.append((netData[6][i], netData[7][i]))

netMapInfo = []
for z in range(len(netData[0])):
	marker ={
			'icon': 'http://www.google.com/mapfiles/marker.png',
			'lat': float(netData[6][z]),
			'lng': float(netData[7][z]),
			'infobox': '<b>SSID: '+str(netData[1][z])+' || Encrypt: '+str(netData[4][z])+' || Packets: '+str(netData[2][z])+'</b>'
		}
	netMapInfo.append(marker)

@app.route("/")
def main():
	mymap=Map(
		identifier="mymap",
		lat=netData[6][0],
		lng=netData[7][0],
		markers=netMapInfo,
		style="height:700px;width:700px;margin:0;"
	)
	
	return( render_template("map.html", mymap=mymap) )


if __name__ == "__main__":
	app.run(debug=True)
