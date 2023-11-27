from Empleado import Empleado

class Gerente(Empleado):                          #Herencia
    def __init__(self, nombre, edad, dni, salario, cargo, departamento,emp_a_cargo, bono_objectivo):
        super().__init__(nombre, edad, dni, salario, cargo) 
        self.departamento = departamento
        self.emp_a_cargo = emp_a_cargo
        self.bono_objetivo = bono_objectivo
        
    def mostrar_info(self):
        return f"Nombre: {self.nombre} Edad: {self.edad} DNI:{self._dni} Salario: {self._salario} cargo: {self.cargo} Departamento: {self.departamento} Empleados a cargo: {self.emp_a_cargo}"
    
    def consultar_salario(self):
            return f"El salario base de Gerente es de: $ {self._salario}"
        
    def calcular_salario(self):                     #Polimorfismo
        if self.cargo == "Gerente":
            nvo_salario_gte = super().calcular_salario() + self.bono_objetivo
            return nvo_salario_gte
        else:
            return "El empleado no es gerente" 