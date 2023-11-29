"""Escribe un programa que intente abrir un archivo, leer su contenido y luego cerrarlo. 
Utiliza bloques try, except y finally para asegurarte de que el archivo se cierre correctamente,
incluso si ocurre una excepción durante la lectura."""

archivo = None 

try:
    with open("archivo.txt", "r") as archivo:
        contenido = archivo.read()
        print("Contenido del archivo:")
        print(contenido)

except FileNotFoundError:
    print("Error: El archivo no existe.")

except Exception as e:
    print(f"Error: Se produjo una excepción - {type(e).__name__}: {e}")

finally:
    if archivo and not archivo.closed:
        archivo.close()
        print("Archivo cerrado correctamente.")