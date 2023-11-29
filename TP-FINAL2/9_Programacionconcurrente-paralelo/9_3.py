"""Crea dos procesos utilizando la biblioteca multiprocessing y ejecuta funciones diferentes 
en cada proceso."""

import multiprocessing

def correr():
    print("Esta funcion es para correr")

def saltar():
    print("Esta funcion es para saltar")

if __name__ == '__main__':
    proceso1 = multiprocessing.Process(target=correr)
    proceso2 = multiprocessing.Process(target=saltar)

    proceso1.start()
    proceso2.start()

    proceso1.join()
    proceso2.join()
