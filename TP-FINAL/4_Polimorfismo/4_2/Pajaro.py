from Animal import Animal

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