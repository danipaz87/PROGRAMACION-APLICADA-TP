"""Hacer un decorador para verificar las precondiciones antes de ejecutar una función."""
def verif_cond_div(funcion):
    def wrapper(*args, **kwargs):
        for div in args:
            if div > 0:
                print("El resultado es positivo")
            elif div < 0: 
                print("El resultado es negativo")
            else:
                print("El resultado es cero o no se puede realizar la divición")

        return funcion(*args, **kwargs)
    return wrapper

@verif_cond_div
def div(a,b):
    return a/b

print(div(-5,1))