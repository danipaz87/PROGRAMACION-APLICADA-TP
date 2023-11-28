"""Toma una lista de cadenas y utiliza map con una función lambda para convertir todas las cadenas 
en mayúsculas."""

cadenas = ["Hola", "Profe", "Bonini", "Queremos promocionar", "Carita feliz"]

mayuscula = list(map(lambda x: x.upper(), cadenas))

print(mayuscula)