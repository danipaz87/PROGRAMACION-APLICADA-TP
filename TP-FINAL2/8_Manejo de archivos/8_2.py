"""Escribe un programa que abra un archivo de texto, cuente cuántas palabras contiene y muestre 
el resultado en la pantalla."""

def contar_palabras(archivo_texto):
    try:
        with open(archivo_texto, "r"):
            contenido = archivo_texto.read()

            palabras = contenido.split()
            cantidad_palabras = len(palabras)

            return cantidad_palabras

    except FileNotFoundError:
        print(f"Error: El archivo {archivo_texto} no existe.")

    except Exception:
        print(f"Error inesperado: {type(Exception).__name__}: {Exception}")

    finally:
        print("Operación completada o error bajo control")

try:
    archivo_texto ="archivo_texto.txt"

    cantidad_palabras = contar_palabras(archivo_texto)

    if cantidad_palabras is not None:
        print(f"El archivo {archivo_texto} contiene {cantidad_palabras} palabras.")

except Exception:
    print(f"Error inesperado: {type(Exception).__name__}: {Exception}")