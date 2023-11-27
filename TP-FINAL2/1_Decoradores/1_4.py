"""Hacer un decorador para verificar las precondiciones antes de ejecutar una función."""

import functools

def verificar_precondiciones(precondiciones):
    def decorador(funcion):
        def wrapper(*args, **kwargs):
            # Verifica las precondiciones
            for precondicion in precondiciones:
                if not precondicion(*args):
                    raise ValueError(f"La precondición {precondicion.__name__} no se cumple")

            # Devuelve el resultado de la función
            resultado = funcion(*args, **kwargs)
            return resultado

        return wrapper

    return decorador

@verificar_precondiciones([
    lambda x, y: x >= 0 and y >= 0,
    lambda longitud_args: longitud_args >= 2,
])
def sumar(x, y):
    return x + y

print(sumar(1, 2))