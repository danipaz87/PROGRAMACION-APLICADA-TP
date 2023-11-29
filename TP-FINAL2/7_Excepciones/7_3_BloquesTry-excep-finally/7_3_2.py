"""Crea un programa que solicite al usuario dos números y una operación matemática (suma, resta,
multiplicación, división) para realizar. Utiliza bloques try, except y finally para manejar 
cualquier excepción que pueda ocurrir durante la operación y asegurarte de que los recursos se 
liberen correctamente."""

num1 = float(input("Introducir el primer número: "))
num2 = float(input("Introducir el segundo número: "))
operacion = input("Introducir el tipo de operacion: (suma, resta, multiplicación, división): ")

try:
    if operacion == "suma":
        resultado = num1 + num2
    elif operacion == "resta":
        resultado = num1 - num2
    elif operacion == "multiplicación":
        resultado = num1 * num2
    elif operacion == "división":
        resultado = num1 / num2

    print(f"Resultado: {resultado}")

except ValueError:
    print("No se puede convertir una cadena en un número")
except ZeroDivisionError:
    print("El segundo número no puede ser cero")
finally:
    print("Operacion Finalizada")