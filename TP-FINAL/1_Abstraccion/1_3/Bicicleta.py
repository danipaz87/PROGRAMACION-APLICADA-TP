from Vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima):
        super().__init__(marca, modelo, velocidad_maxima)

    def arrancar(self):
        return "La bicicleta arranca cuando se comieza a pedalear."

    def frenar(self):
        return "La Bicleta esta detenida , se ha dejado de pedalear"  