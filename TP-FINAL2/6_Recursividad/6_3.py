"""Escribe una función recursiva para invertir una cadena."""

def invertir_cadena(cadena):
    if len(cadena) <= 1:
        return cadena
    
    return cadena[-1] + invertir_cadena(cadena[1:-1]) + cadena[0]

cadena_a_invertir= "Programacion Aplicada"

cadena_invertida = invertir_cadena(cadena_a_invertir)

print(f"Cadena a invertir:\n{cadena_a_invertir}")
print(f"Cadena Invertida:\n{cadena_invertida}")
    