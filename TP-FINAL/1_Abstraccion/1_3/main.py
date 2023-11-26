from Coche import Coche
from Motocicleta import Motocicleta
from Bicicleta import Bicicleta

coche=Coche("Renault","Clío",200)
print("-----------Coche---------------")
print(coche.arrancar())
print(coche.frenar())

moto=Motocicleta("Bera","X28",150)
print("-----------Motocicleta---------------")
print(moto.arrancar())
print(moto.frenar())

bici=Bicicleta("BMC","TRX25",50)
print("-----------Bicicleta---------------")
print(bici.arrancar())
print(bici.frenar())