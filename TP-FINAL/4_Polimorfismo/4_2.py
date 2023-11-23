"""Animal: Utilizar la clase Animal del ejercicio de herencia y aplicar polimorfismo para realizar el sonido 
característico del animal. Luego, crear una lista de animales de diferentes tipos y utilizar el polimorfismo
para hacer que emiten sus sonidos."""

class Animal:
    def __init__(self, nombre , edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostrar_datos_animal(self):
        pass
        
    def hacer_sonido(self):
        return "El animal esta emitiendo sonido" 
    
    def hacer_movimiento(self):
        pass
    
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza
        
    def mostrar_datos_animal(self):
        return f"Mi mascota: {self.nombre} , su edad es de: {self.edad} años y su raza: {self.raza}"
    
    def hacer_sonido(self):
        return "Guauuuu , Guauu "
    
    def hacer_movimiento(self):
        return "El Perro corre"
    
class Gato(Animal):
    def __init__(self, nombre, edad, pelaje):
        super().__init__(nombre, edad)
        self.pelaje= pelaje
        
    def mostrar_datos_animal(self):
        return f"Mi mascota: {self.nombre} , su edad es de: {self.edad} años y su pelaje: {self.pelaje} "
        
    def hacer_sonido(self):
        return "Miau , Miauu"
    
    def hacer_movimiento(self):
        return "El gato juega"
    
class Pajaro(Animal):
    def __init__(self, nombre, edad, pico):
        super().__init__(nombre, edad)
        self.pico = pico
    
    def mostrar_datos_animal(self):
        return f"Mi mascota: {self.nombre} , su edad es de: {self.edad} años y su pico: {self.pico}"
        
    def hacer_sonido(self):
        return "Hola !! Holaa !!"
    
    def hacer_movimiento(self):
        return "El loro vuela"
    
animales = [
Perro("Potota", 5, "Mestiza"),
Gato("Mecha", 3, "Corto"),
Pajaro("Cucu",1 , "Largo")
]

for animal in animales:
    print(animal.mostrar_datos_animal())
    print(f"{animal.nombre} hace el sonido: {animal.hacer_sonido()} ")
    print(animal.hacer_movimiento())
