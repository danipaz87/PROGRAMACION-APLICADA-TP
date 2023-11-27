class Departamento:
    def __init__(self):
        self.empleados = []
    
    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
    
    def eliminar_empleado(self, empleado):
        self.empleados.remove(empleado)
    
    def consultar_empleado(self):
        for empleado in self.empleados:
            return self.empleados