#!/usr/bin/env python3

from RFXtrx import PySerialTransport
from RFXtrx import SensorEvent
from time import sleep
import sys

transport = PySerialTransport('/dev/ttyUSB0')
transport.connect()
transport.reset()

id=sys.argv[1]

while True:
    event = transport.receive_blocking()
    if event is not None and isinstance(event, SensorEvent):
        if event.device.id_string == id:
            sys.stdout.write(str(event.values.get('Temperature')))
            sys.stdout.flush()
            sys.exit(0)

