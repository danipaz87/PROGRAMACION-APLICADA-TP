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