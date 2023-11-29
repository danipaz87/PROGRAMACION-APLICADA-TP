"""Escribe un programa que tome varios archivos de texto y los concatena en un solo archivo de salida.
Asegúrate de cerrar todos los archivos correctamente."""

archivos_entrada = ["archivo1.txt", "archivo2.txt", "archivo3.txt"]
archivo_salida = "archivo_concatenado.txt"

try:
    with open(archivo_salida, 'w') as f_out:
        for archivo in archivos_entrada:
            try:
                with open(archivo, 'r') as f_in:
                    f_out.write(f_in.read() + '\n')
            except FileNotFoundError:
                print(f"Advertencia: El archivo {archivo} no existe. No se incluirá en la concatenación.")

    print(f"Archivos {archivos_entrada} concatenados en {archivo_salida}.")

except Exception:
    print(f"Error inesperado: {type(Exception).__name__}: {Exception}")