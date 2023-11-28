"""Dada una lista de cadenas, utiliza map y una función lambda para crear una lista con la longitud 
de cada palabra."""

cadenas = ["Hola", "Profe", "Bonini", "Queremos promocionar", "Carita feliz"]

longitud = list(map(lambda x: len(x), cadenas))

print(longitud)