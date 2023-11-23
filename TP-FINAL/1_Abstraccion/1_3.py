"""Vehiculo: Implementar las clases Vehiculo, Coche, Motocicleta y Bicicleta. La clase Vehiculo debe tener 
propiedades como marca, modelo y velocidad_maxima. Cada subclase debe definir sus métodos y
atributos específicos relacionados con el comportamiento de cada tipo de vehículo."""

class Vehiculo:
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca=marca
        self.modelo=modelo
        self.velocidad_maxima=velocidad_maxima

    def arrancar():
        pass
    
    def frenar():
        pass


class Coche(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima):
        super().__init__(marca, modelo, velocidad_maxima)

    def arrancar(self):
        return "El coche arranca cuando se pone en marcha el motor."
    
    def frenar(self):
        return "El coche esta detenido"


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima):
        super().__init__(marca, modelo, velocidad_maxima)
    
    def arrancar(self):
        return "La motocicleta arranca cuando se pone en marcha el motor." 
    
    def frenar(self):
        return "La Motocicleta esta detenida"   


class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima):
        super().__init__(marca, modelo, velocidad_maxima)

    def arrancar(self):
        return "La bicicleta arranca cuando se comieza a pedalear."

    def frenar(self):
        return "La Bicleta esta detenida , se ha dejado de pedalear"  

coche=Coche("Renault","Clío",200)
print(coche.arrancar())
print(coche.frenar())

moto=Motocicleta("Bera","X28",150)
print(moto.arrancar())
print(moto.frenar())

bici=Bicicleta("BMC","TRX25",50)
print(bici.arrancar())
print(bici.frenar())