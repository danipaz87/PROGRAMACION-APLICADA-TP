"""Escribe un programa que abra un archivo de entrada, lea su contenido y luego escriba ese contenido
en un nuevo archivo de salida. Asegúrate de cerrar ambos archivos al final."""

def copiar_archivo(archivo_entrada, archivo_salida):
    try:
        with open(archivo_entrada, "r"):
            contenido = archivo_entrada.read()
            
        with open(archivo_salida, "w"):
            archivo_salida.write(contenido)

    except FileNotFoundError:
        print(f"Error: El archivo {archivo_entrada} no existe.")

    except Exception as e:
        print(f"Error inesperado: {type(e).__name__}: {e}")

    finally:
        print("Operación completada o error bajo control.")
        try:
            archivo_entrada.close()
            archivo_salida.close()
        except:
            pass

try:
    archivo_entrada = "archivo_entrad.txt"
    archivo_salida = "archivo_salida.txt"

    copiar_archivo(archivo_entrada, archivo_salida)

except Exception:
    print(f"Error inesperado: {type(Exception).__name__}: {Exception}")