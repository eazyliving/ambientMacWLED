#!/bin/bash

DISPLAY=1

while :
do

screencapture -D $DISPLAY -T 0 -r -mx /tmp/ambient.png
python dcolor.py
sleep 2

done