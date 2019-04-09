#!/bin/bash

echo "[*] Starting Scout Map Server"

IP=$(ifconfig | grep inet | grep -v 127.0.0.1 | grep -v inet6 | grep -m 1 inet | awk -F' ' '{print $2}')

FLASK_APP=ifaceScout.py flask run --host=$IP


