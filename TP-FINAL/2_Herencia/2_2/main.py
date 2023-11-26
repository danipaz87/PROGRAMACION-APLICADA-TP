from Gerente import Gerente
from Trabajador import Trabajador


gerente = Gerente(nombre="Leonardo Caldas", salario=950000, departamento="Gerencia", empleados_a_cargo="10")
print("-----------Gerente-----------------")
print(gerente.mostrar_empleado())
print(gerente.tipo_empleado())

trabajador = Trabajador("Cristian Augusto", 450000, "Consultoria", "Consultor de Software")
print("-----------Trabajador---------------")
print(trabajador.mostrar_empleado())
print(trabajador.tipo_empleado())