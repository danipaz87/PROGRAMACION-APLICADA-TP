from Vehiculo import Vehiculo

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima):
        super().__init__(marca, modelo, velocidad_maxima)
    
    def arrancar(self):
        return "La motocicleta arranca cuando se pone en marcha el motor." 
    
    def frenar(self):
        return "La Motocicleta esta detenida"  