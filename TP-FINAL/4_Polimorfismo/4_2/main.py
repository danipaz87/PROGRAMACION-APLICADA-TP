from Perro import Perro
from Gato import Gato 
from Pajaro import Pajaro
    
animales = [
Perro("Potota", 5, "Mestiza"),
Gato("Mecha", 3, "Corto"),
Pajaro("Cucu",1 , "Largo")
]

for animal in animales:
    print(animal.mostrar_datos_animal())
    print(f"{animal.nombre} hace el sonido: {animal.hacer_sonido()} ")
    print(animal.hacer_movimiento())
