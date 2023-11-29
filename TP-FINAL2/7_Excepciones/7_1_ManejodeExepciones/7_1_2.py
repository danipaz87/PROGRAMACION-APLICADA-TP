"""Crea una lista de números y, a continuación, intenta acceder a un elemento en un índice 
especificado por el usuario. Utiliza un bloque try y except para manejar la excepción que se produce 
si el índice está fuera de rango."""

lista = [0,3,4,5,6]
    
indice = int(input("Ingrese numero del indice:"))

try:
    numero = lista[indice]
    
    print(f"El elemento en el indice {indice} es {numero}")
    
except IndexError:
    
    print(f"El indice {indice} esta fuera de rango")