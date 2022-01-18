#!/bin/bash
co2=$( tail -n 1 /home/pi/log/log.txt )
python3 beeper.py "$co2"
