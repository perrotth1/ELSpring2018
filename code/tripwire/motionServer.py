from flask import Flask
from flask import render_template
import sqlite3 as mydb
import os

app = Flask(__name__)

@app.route("/")
def display():
	con = mydb.connect("motionLog.db")
	with con:
		try:
			cur = con.cursor()
			cur.execute("SELECT * FROM motions ORDER BY rowid DESC LIMIT 10")
			data = cur.fetchall()
		except (Error) as e:
			print("ERROR")
			print(e)

	return render_template("template.html", db=data)

if __name__ == "__main__":
	while true:
		app.run(debug=True)
