#!/bin/bash
#
#
#
source ~/pyRFXtrx/bin/activate
cd ~/brewing
nohup  ./set_temp.sh > ./log.txt 2>&1  &
