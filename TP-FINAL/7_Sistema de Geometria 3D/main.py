from Punto3D import Punto3D
from Cubo import Cubo
from Esfera import Esfera
from Cilindo import Cilindro

punto1 = Punto3D(2, 3, 4)
cubo1 = Cubo(punto1, 4)
esfera1 = Esfera(punto1, 3)
cilindro1 = Cilindro(punto1, 3, 4)

print("-----------Cubo--------------------------")
print("Volumen:", cubo1.calcular_volumen())
print("Area superficial: ", cubo1.calcular_area_superficial())
print("----------------Esfera-------------------")
print("Volumen: ", esfera1.calcular_volumen())
print("Area superficial:", esfera1.calcular_area_superficial())
print("------------Cilindro---------------------")
print("Volumen: ", cilindro1.calcular_volumen())
print(f"Area superficial:  {cilindro1.calcular_area_superficial}")