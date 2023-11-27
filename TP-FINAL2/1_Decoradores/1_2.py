"""Hacer un decorador para verificar que los argumentos de una función sean del tipo correcto."""

def verificar_argumentos(tipos_correctos):
    
    def decorador(funcion):
        
        def wrapper(*args , **kwargs):
            for argumento, tipo_argumento in zip(args, tipos_correctos):
                if not isinstance(argumento, tipo_argumento):
                    raise TypeError(f"El argumento {argumento} debe ser de tipo {tipos_correctos}")

            
            resultado = funcion(*args, **kwargs)

            return resultado

        return wrapper

    return decorador

@verificar_argumentos([int, int])
def sumar(a,b):
    return a + b

print(f"Resultado:" , sumar(4,5))