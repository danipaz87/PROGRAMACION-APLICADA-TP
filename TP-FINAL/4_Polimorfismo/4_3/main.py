from Trabajador import Trabajador
from Gerente import Gerente

empleados  = [Gerente(nombre="Leonardo Caldas", salario=950000, departamento="Gerencia", empleados_a_cargo="10"),
            Trabajador("Cristian Augusto", 450000, "Consultoria", "Asesorar clientes sobre el uso del sistema", True)] 

for empleado in empleados: 
    print(empleado.mostrar_empleado())
    print(empleado.tipo_empleado())
    print(f"Sueldo Calculado:" , empleado.calcular_salario())