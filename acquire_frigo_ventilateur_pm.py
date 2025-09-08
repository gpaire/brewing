#!/usr/bin/env python3

from RFXtrx import PySerialTransport
from RFXtrx import LightingDevice
from time import sleep
import logging

import pickle




def afficher_attributs(objet):
    """
    Affiche tous les attributs publics d'un objet avec leurs valeurs.
    """
    print(f"Attributs de l'objet {type(objet).__name__} :")
    for attr in dir(objet):
        if not attr.startswith("__"):
            try:
                valeur = getattr(objet, attr)
                print(f"{attr} = {valeur}")
            except Exception as e:
                print(f"{attr} = <erreur: {e}>")





def decharger_objet(objet, chemin_fichier):
    """
    Sauvegarde un objet Python dans un fichier avec pickle.
    """
    with open(chemin_fichier, "wb") as f:
        pickle.dump(objet, f)
    print(f"Objet sauvegardé dans {chemin_fichier}")



def charger_objet(chemin_fichier):
    """
    Charge un objet Python depuis un fichier pickle.
    """
    with open(chemin_fichier, "rb") as f:
        objet = pickle.load(f)
    print(f"Objet chargé depuis {chemin_fichier}")
    return objet



transport = PySerialTransport('/dev/ttyUSB0')
transport.connect()
transport.reset()

while True:
    event = transport.receive_blocking()
    if event is not None and isinstance(event.device, LightingDevice):
        #sleep(5)
        event.device.send_off(transport)
        ack = transport.receive_blocking()
        event.device.send_on(transport)
        event.device.send_off(transport)
        event.device.send_on(transport)
        event.device.send_off(transport)
        print("=======================")
        afficher_attributs(transport)
        print("-----------------------")
        afficher_attributs(event)
        print("-----------------------")
        afficher_attributs(ack)
        print("~~~~~~~~~~~~~~~~~~~~~~~")
        decharger_objet(event,'./frigo_ventilateur_pm')
