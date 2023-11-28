"""Dada una lista de números, utiliza map y una función lambda para crear una nueva lista que 
contenga el doble de cada número."""

lista = [0,3,4,5,6]

doble = list(map(lambda x: x*2, lista))

print(doble)