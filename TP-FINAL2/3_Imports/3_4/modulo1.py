"""Crear dos módulos en el mismo directorio. Desde un módulo, importa una función o variable del otro utilizando una 
importación absoluta y generar un error de importación circular."""

from modulo2 import frenar

def arrancar():
    return "El coche arranca cuando se pone en marcha el motor." 


    