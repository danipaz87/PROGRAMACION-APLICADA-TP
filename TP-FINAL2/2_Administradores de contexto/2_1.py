"""Hacer un administrador de contexto para notificar eventos al entrar y al salir de un bloque 
de código."""

class NotificarEntradaSalidaContexto:
    def __init__(self):
        pass

    def __enter__(self):
        print("Cambiando el directorio a la ruta 9")
        return self

    def __exit__(self, type, value, traceback):
        print("Volviendo al directorio original")


with NotificarEntradaSalidaContexto():
    a = 2 + 2
    print(f"Resultado:, {a}")