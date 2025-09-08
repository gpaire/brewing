#!/usr/bin/env python3

import sys
import logging


import RFXtrx
import time


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
