from flask import Flask
from flask import render_template
from datetime import time
import sqlite3 as mydb 
import os
import time
 
app = Flask(__name__)
 
 
@app.route("/temp_chart")
def chart():
	con = mydb.connect("tTemp.db")
	
	with con:
		try:
			cur = con.cursor()
			legend = 'Celcius'
			labels = []
			values = []

			for row in cur.execute("SELECT C FROM tTemp"):
				values.append(float(row[0]))
			for row in cur.execute("SELECT time FROM tTemp"):
				labels.append(str(row[0]))

		except (Error) as e:
			print ("ERROR")
			print (e)

	return render_template('chart.html', values=values, labels=labels, legend=legend)
 
 
if __name__ == "__main__":
	while true:
		app.run(debug=True)
	
