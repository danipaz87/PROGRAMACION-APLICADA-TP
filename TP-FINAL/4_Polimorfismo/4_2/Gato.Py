from Animal import Animal

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