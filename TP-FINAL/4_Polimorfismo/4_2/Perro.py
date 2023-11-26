from Animal import Animal

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