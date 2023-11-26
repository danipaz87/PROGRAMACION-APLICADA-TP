from Vehiculo import Vehiculo

class Coche(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima):
        super().__init__(marca, modelo, velocidad_maxima)

    def arrancar(self):
        return "El coche arranca cuando se pone en marcha el motor."
    
    def frenar(self):
        return "El coche esta detenido"