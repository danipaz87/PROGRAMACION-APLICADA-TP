"""Hacer un decorador para registrar las llamadas a una función, junto con sus argumentos y resultados."""

def registrar_llamadas(funcion):
    
    def wrapper(*args , **kwargs):
        print(f"LLamado a la funcion: {funcion.__name__}")
    
        resultado = funcion(*args , **kwargs)
        print(f"El resultado es: {resultado}")
        
        return resultado
    
    return wrapper

@registrar_llamadas
def sumar(a ,b):
    return a + b

resultado_sumar = sumar(3,5)
print("El reultado de la suma es de:", resultado_sumar)
