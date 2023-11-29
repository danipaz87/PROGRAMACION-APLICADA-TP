"""Implementa el problema del productor-consumidor utilizando hilos, donde un hilo produce datos y 
otro hilo los consume desde una cola compartida."""

import threading
import queue
import time

cola = queue.Queue(maxsize=5)

def productor():
    for i in range(10):
        item = f"elemento-{i}"
        cola.put(item)
        print(f"Producido {item}")
        time.sleep(1)

def consumidor():
    while not cola.empty():
        item = cola.get()
        print(f"Consumido {item}")
        time.sleep(2)

hilo_productor = threading.Thread(target=productor)
hilo_consumidor = threading.Thread(target=consumidor)

hilo_productor.start()
hilo_consumidor.start()

hilo_productor.join()
hilo_consumidor.join()

print("Proceso terminado")
