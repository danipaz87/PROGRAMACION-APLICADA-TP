"""Escribe un programa que abra un archivo, lea su contenido y escriba el mismo contenido en otro 
archivo. Utiliza bloques try,except y finally para manejar cualquier excepción que pueda
ocurrir durante la lectura o escritura, y asegúrate de que ambos archivos se cierren correctamente."""

def copiar_archivo(archivo_original, archivo_copia):
    try:
        archivo_origen = open(archivo_original, "r")
        
    except FileNotFoundError:
        print(f"El archivo de origen '{archivo_original}' no existe")
        return

    try:
        archivo_destino = open(archivo_copia, "w")

    except FileNotFoundError:
        print(f"El archivo de destino '{archivo_copia}' no existe")
        return

    archivo_destino.write(archivo_original.read())

    archivo_original.close()
    archivo_copia.close()


copiar_archivo("archivo_original.txt", "archivo_copia.txt")