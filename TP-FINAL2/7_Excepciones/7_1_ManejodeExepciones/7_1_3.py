"""Solicita al usuario que ingrese una cadena que represente un número. Utiliza un bloque try y 
except para manejar la excepción que se produce si la cadena no se puede convertir a un número."""

def convertir(cadena):
    try:
        return int(cadena)
    except ValueError:
        return None
    
num_cadena = input("Introducir cadena:")

numero = convertir(num_cadena)

if numero is not None:
    print(f"El numero es {numero}")
else:
    print("La cadena no se puede convertir a un numero")