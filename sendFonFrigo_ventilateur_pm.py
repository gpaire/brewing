#!/usr/bin/env python3

from RFXtrx import PySerialTransport
from RFXtrx import LightingDevice
from time import sleep
import logging

import pickle




def charger_objet(chemin_fichier):
    """
    Charge un objet Python depuis un fichier pickle.
    """
    with open(chemin_fichier, "rb") as f:
        objet = pickle.load(f)
    print(f"Objet chargé depuis {chemin_fichier} - ON")
    return objet

transport = PySerialTransport('/dev/ttyUSB0')
transport.connect()
transport.reset()

event=charger_objet('./frigo_ventilateur_pm')
event.device.send_on(transport)
