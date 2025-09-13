#!/usr/bin/env python3

import sys
import logging


import RFXtrx
import time
class Tee:
    def __init__(self, *streams):
        self.streams = streams
    def write(self, data):
        for s in self.streams:
            try:
                s.write(data)
            except ValueError:
                # Ignore closed streams
                pass
    def flush(self):
        for s in self.streams:
            try:
                s.flush()
            except ValueError:
                pass

# Open file for the duration of the program
log_file = open("log.txt", "w")

# Wrap stdout and stderr
sys.stdout = Tee(sys.stdout, log_file)
sys.stderr = Tee(sys.stderr, log_file)

print("This goes to screen AND file")

# Example of caught exception
try:
    raise ValueError("Error also goes to screen AND file")
except ValueError as e:
    print("Caught exception:", e)

def print_callback(event):
    print(event)

def main():
    logging.basicConfig(level=logging.DEBUG)

    if len(sys.argv) >= 2:
        rfxcom_device = sys.argv[1]
    else:
        rfxcom_device = '/dev/serial/by-id/usb-RFXCOM_RFXtrx433_A1Y0NJGR-if00-port0'

    modes_list = sys.argv[2].split() if len(sys.argv) > 2 else None
    print ("modes: ", modes_list)
    core = RFXtrx.Connect(RFXtrx.PySerialTransport(rfxcom_device), print_callback, modes=modes_list)
    core.connect()

    print (core)
    while True:
        print(core.sensors())
        time.sleep(2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass








# Program ends: now safe to close the file
log_file.close()
