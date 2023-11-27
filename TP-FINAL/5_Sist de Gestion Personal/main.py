from Empleado import Empleado
from Gerente import Gerente
from Departamento import Departamento

empleado = Empleado("Marisa Perez", 40 , 15465897, 85000, "Vendedor")
gerente = Gerente("Andres La Civita",50,16123852,95000,"Gerente","Gerencia", 10 , 50000)

departamento = Departamento()

departamento.agregar_empleado(empleado)
departamento.agregar_empleado(gerente)

print("-----------------Empleados--------------------------")
empleado_departamento = departamento.consultar_empleado()
for empleado in empleado_departamento:
    print(empleado.mostrar_info())

print("------------------Salarios--------------------------")


print(gerente.consultar_salario())
print(f"Salario Final:" , gerente.calcular_salario())

print("--------------Eliminando Empleado-------------------")
print(gerente.mostrar_info())
departamento.eliminar_empleado(gerente)
print("-----------------Empleados--------------------------")
empleado_departamento = departamento.consultar_empleado()
for empleado in empleado_departamento:
    print(empleado.mostrar_info())
