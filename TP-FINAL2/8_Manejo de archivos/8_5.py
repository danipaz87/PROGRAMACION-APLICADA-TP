"""Lee un archivo CSV que contiene registros de datos y convertirlo en un archivo JSON."""

import csv
import json

csv_file = 'data.csv'
json_file = 'data.json'

try:
    data = []
    with open(csv_file, newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            data.append(row)

    with open(json_file, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

    print(f"Archivo {csv_file} convertido a {json_file}.")

except FileNotFoundError:
    print(f"Error: El archivo {csv_file} no existe.")

except Exception:
    print(f"Error inesperado: {type(Exception).__name__}: {Exception}")