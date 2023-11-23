"""Animal: Utilizar las clases Animal, Perro, Gato y Pájaro. Se debe incluir atributos como nombre y edad. 
Las subclases deben heredar y definir métodos y atributos relacionados con el comportamiento y características
de cada tipo de animal."""

class Animal:
    def __init__(self, nombre , edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostrar_datos_animal(self):
        pass
        
    def hacer_sonido(self):
        pass 
    
    def hacer_movimiento(self):
        pass
    
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza
        
    def mostrar_datos_animal(self):
        return f"Mi mascota: {perro.nombre} su edad es de: {perro.edad} y su raza: {perro.raza}"
    
    def hacer_sonido(self):
        return "El perro ladra"
    
    def hacer_movimiento(self):
        return "El Perro corre"
    
class Gato(Animal):
    def __init__(self, nombre, edad, pelaje):
        super().__init__(nombre, edad)
        self.pelaje= pelaje
        
    def mostrar_datos_animal(self):
        return f"Mi mascota: {gato.nombre} su edad es de: {gato.edad} y su pelaje: {gato.pelaje} "
        
    def hacer_sonido(self):
        return "El gato maulla"
    
    def hacer_movimiento(self):
        return "El gato juega"
    
class Pajaro(Animal):
    def __init__(self, nombre, edad, pico):
        super().__init__(nombre, edad)
        self.pico = pico
    
    def mostrar_datos_animal(self):
        return f"Mi mascota: {pajaro.nombre} su edad es de: {pajaro.edad} y su pico: {pajaro.pico}"
        
    def hacer_sonido(self):
        return "El loro canta"
    
    def hacer_movimiento(self):
        return "El loro vuela"
    
perro = Perro("Potota", 5, "Mestiza")
print(perro.mostrar_datos_animal())
print(perro.hacer_sonido())
print(perro.hacer_movimiento())

gato = Gato("Mecha", 3, "Corto")
print(gato.mostrar_datos_animal())
print(gato.hacer_sonido())
print(gato.hacer_movimiento())

pajaro = Pajaro("Cucu",1 , "Largo")
print(pajaro.mostrar_datos_animal())
print(pajaro.hacer_sonido())
print(pajaro.hacer_movimiento())

