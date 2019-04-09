#!/bin/bash

#For crontab to start SUPPON at startup

cd ELSpring2019/Suppon/

sleep 10

python switchStart.py &

sleep 2

#python shutDownSwitch.py &
