"""Crea dos hilos que ejecuten dos funciones diferentes simultáneamente y muestran mensajes de salida."""

import threading

def hilo_1():
    for i in range(10):
        print("Trabajo Practico - Parte 1")

def hilo_2():
    for i in range(10):
        print("Trabajo Practico - Parte 2")

hilo_1 = threading.Thread(target=hilo_1)
hilo_2 = threading.Thread(target=hilo_2)

hilo_1.start()
hilo_2.start()

hilo_1.join()
hilo_2.join()