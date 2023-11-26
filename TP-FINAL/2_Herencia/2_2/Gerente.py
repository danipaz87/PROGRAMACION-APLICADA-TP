from Empleado import Empleado

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento, empleados_a_cargo):
        super().__init__(nombre, salario, departamento)
        self.empleados_a_cargo = empleados_a_cargo

    def mostrar_empleado(self):
        return f"Nombre: {self.nombre}, Salario: ${self.salario}, Departamento: {self.departamento} , Cantidad de empleados: {self.empleados_a_cargo}"
    
    def tipo_empleado(self):
        return "El tipo de empleado es : Gernete General"  