#!/bin/bash

#This script checks if there are previous logs and if so, saves them to savedLogs/

if find "kismetLogs" -mindepth 1 -print -quit 2>/dev/null | grep -q .; then
	"[!] Previous logs found, saving to savedLogs/"
	sudo mv kismetLogs/* savedLogs
fi



