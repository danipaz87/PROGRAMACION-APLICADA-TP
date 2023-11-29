"""Escribe un programa que solicite al usuario dos números y realice la división de uno por el otro. 
Utiliza un bloque try y except para manejar la excepción que ocurre si el segundo número es cero."""

try:
    numero1 = float(input("Introducir un numero: "))
    numero2 = float(input("Introducir otro numero: "))
    
    division = numero1 / numero2
    
    print(f"Resultado: {division}")
    
except ZeroDivisionError:
    print("El segundo numero no puede ser 0 ")