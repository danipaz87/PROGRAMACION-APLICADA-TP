"""Escribe un programa que intente abrir un archivo que no existe y utilice un bloque try y except 
para manejar la excepción de "FileNotFoundError"."""

def abrir_archivo(nombre_archivo):
    try:
        return open(nombre_archivo, "r")
    except FileNotFoundError:
        return None


archivo = abrir_archivo("archivo_que_no_existe.txt")

if archivo is not None:
    contenido = archivo.read()
    print(contenido)
else:
    print("El archivo no existe")