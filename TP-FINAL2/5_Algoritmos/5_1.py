"""Escribe una función que sume los dígitos de un número pares de un número entero. Si el número es impar, restarle 3 y 
sumarlo. Si el número da negativo, sumar 1."""

def sumar_pares(numero):
    if numero % 2 == 0:
        suma = sum(int(digito) for digito in str(numero))
    elif numero % 2 == 1:
        resultado = (numero - 3)
        if numero < 0:
            numero += 1
        return numero
    return suma


numero_a_calcular = 22
resultado = sumar_pares(numero_a_calcular)
print(f"El resultado para el número {numero_a_calcular} es: {resultado}")
    