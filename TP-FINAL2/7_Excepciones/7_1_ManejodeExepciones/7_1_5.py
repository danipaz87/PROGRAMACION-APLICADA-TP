"""Crea un diccionario y luego intenta acceder a un valor utilizando una clave que no está en el 
diccionario. Utiliza un bloque try y except para manejar la excepción que se produce si la clave no
existe."""

def acceder_a_valor_diccionario(diccionario, clave):
    try:
        return diccionario[clave]
    except KeyError:
        return None


diccionario = {
    "Marca": "Renault",
    "Modelo": "Duster",
    "Año": 2014
}

valor = acceder_a_valor_diccionario(diccionario, "clave_no_existe")

if valor is not None:
    print(valor)
else:
    print("La clave no existe")