"""Escribe una función recursiva para calcular el MCD de dos números enteros."""

def calcular_mcd(x,y):
    if x == 0 or y == 0:
        return x or y
    
    if x == y:
        return x
    
    if x % y == 0:
        return y
    
    return calcular_mcd(y % x , x)

x = 15  
y=20

calcular_mcd = calcular_mcd(x,y)

print(f"Resultado:" , calcular_mcd)