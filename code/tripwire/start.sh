#!/bin/bash

echo "[*] Starting motion detection and server"

IP=$(ifconfig | grep inet | grep -v 127.0.0.1 | grep -v inet6 | grep -m 1 inet | awk -F' ' '{print $2}')

sudo python tripwire.py >>/dev/null &

echo "[*] Motion detection started"

sudo FLASK_APP=motionServer.py flask run --host=$IP

echo "[*] Motion server started"

