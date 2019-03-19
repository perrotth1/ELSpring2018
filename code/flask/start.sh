#!/bin/bash

echo "STARTING TEMP SERVER"

IP=$(ifconfig | grep inet | grep -v 127.0.0.1 | grep -v inet6 | grep -m 1 inet | awk -F' ' '{print $2}')

echo "Starting server on $IP"

sudo ./flaskTemp.py >> log.txt &

sudo FLASK_APP=app.py flask run --host=$IP

PIDA=$(ps -aux | grep -m 1 app.py | awk -F' ' '{print $2}')
PIDB=$(ps -aux | grep -m 1 flaskTemp | awk -F' ' '{print $2}')
PIDC=$(ps -aux | grep -m 2 flaskTemp | awk -F' ' '{print $2}')

while kill -0 $PIDA 2> /dev/null; do sleep 1; done;

echo "KILLING PROCESSES"

sudo kill -9 $PIDB 2> /dev/null
sudo kill -9 $PIDC 2> /dev/null

