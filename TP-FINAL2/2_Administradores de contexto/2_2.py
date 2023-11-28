"""Crea un administrador de contexto que permita cambiar el directorio de trabajo al entrar en un 
bloque y volver al directorio original al salir."""
import os
class AdministradorContexto:
    def __init__(self, nuevo_directorio):
        self.nvo_directorio = nuevo_directorio
        self.directorio = None

    def __enter__(self):
        self.directorio = os.getcwd()
        os.chdir(self.nvo_directorio)
        print(f"Ingresando al nuevo directorio: {self.nvo_directorio}")

    def __exit__(self, exc_type, exc_value, traceback):
        os.chdir(self.directorio)
        print(f"Regresando al directorio original: {self.directorio}")

nvo_directorio = r"C:\Users\Usuario\Desktop\ANALISIS DE SISTEMAS\PROGRAMACION APLICADA"

with AdministradorContexto(nvo_directorio):
    a = 2 + 2
    print(f"Resultado: {a}")