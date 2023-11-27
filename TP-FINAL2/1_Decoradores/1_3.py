"""Hacer un decorador para agregar un retardo antes de que se ejecute una función"""

import time

def agregar_retardo(retardo):

    def decorador(funcion):

        def wrapper(*args, **kwargs):
            time.sleep(retardo)

            resultado = funcion(*args, **kwargs)

            return resultado

        return wrapper

    return decorador

@agregar_retardo(2)
def saludar():
    print("Hola Profesor Bonini")


saludar()