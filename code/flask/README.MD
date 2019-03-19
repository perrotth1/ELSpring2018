Henry Perrottet
Temperature IOT Device

This directory is a collection of scripts and programs that makes up the final stage in the temperature logging assignment,
in which the temperature values are read and displayed in a graph on a web server. I have used the Flask library to serve
the graph, in combination with the Chart.min.js javascript library for drawing graphs. 

Description of Files:
The flaskTemp.py program is the program that reads from the temperature sensor and logs resulst to the tTemp.db database.
The app.py program is the flask program that reads the values from the database file and creates the web server.
The static and templates directories contain the javascript libraries and HTML resources for the line graph. 
The log.txt file is just for logged output from the flaskTemp.py program. 
The start.sh file is a script I made to smoothly start the flaskTemp.py program as well as the app.py flask program. The
script finds the IP address of the local machines network interface through ifconfig and starts the server on that IP. 
It also kills the remaining processes when the main Flask process is exited through a keyboard interrupt. 

TO START:
Just run the start.sh script as root user. Once the server is started, in your browser go to [yourIp]/temp_chart, where
[yourIp] is the IP address that flask is using. It will say in the output when it starts which IP it uses. 
Also, when the server is started it wipes the database, so give the graph some time to start logging temperature values.
After about 10 seconds it will have some results. 

