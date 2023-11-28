"""Toma una lista de números y utiliza map con una función lambda para calcular la raíz cuadrada de 
cada número."""

import math

lista = [0,3,4,5,6]

raiz_cuadrada = list(map(lambda x: math.sqrt(x), lista))

print(raiz_cuadrada)