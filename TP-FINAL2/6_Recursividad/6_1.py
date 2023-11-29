"""Escribe una función recursiva para encontrar y sumar todos los números primos desde 1 hasta un 
número deseado."""

def sum_primos(num):
    if num < 2:
        return False
    
    if num == 2:
        return True
    
    for i in range(3,int(num ** 5) + 1, 2):
        if num % i == 0:
            return False
    
    return True

num = 22
suma = sum_primos(num)
print(f"Resultado: ", suma)