from Animal import Animal
from Perro import Perro
from Gato import Gato
from Pajaro import Pajaro


perro = Perro("Potota", 5, "Mestiza")
print("-----------Perro-----------------")
print(perro.mostrar_datos_animal())
print(perro.hacer_sonido())
print(perro.hacer_movimiento())


gato = Gato("Mecha", 3, "Corto")
print("-----------Gato-----------------")
print(gato.mostrar_datos_animal())
print(gato.hacer_sonido())
print(gato.hacer_movimiento())


pajaro = Pajaro("Cucu",1 , "Largo")
print("-----------Pajaro-----------------")
print(pajaro.mostrar_datos_animal())
print(pajaro.hacer_sonido())
print(pajaro.hacer_movimiento())

