"""Lee un archivo CSV que contiene registros de datos y realiza alguna operación de procesamiento 
en los datos, cómo calcular promedios,encontrar valores máximos o mínimos, o filtrar registros 
que cumplan ciertas condiciones."""

import csv

def calcular_promedio_sueldo(archivo_csv):
    try:
        with open(archivo_csv, newline=''):
            lector_csv = csv.DictReader(archivo_csv)

            total_sueldos = 0
            cantidad_registros = 0

            for fila in lector_csv:
                total_sueldos += int(fila['sueldo'])
                cantidad_registros += 1

            if cantidad_registros > 0:
                promedio = total_sueldos / cantidad_registros
                return promedio
            else:
                return None

    except FileNotFoundError:
        print(f"Error: El archivo {archivo_csv} no existe.")

    except Exception:
        print(f"Error inesperado: {type(Exception).__name__}: {Exception}")

archivo_csv = "datos.csv"

promedio_sueldo = calcular_promedio_sueldo(archivo_csv)

if promedio_sueldo is not None:
    print(f"El promedio de sueldos es: {promedio_sueldo}")