from Persona import Persona

class Empleado(Persona):                       #Herencia     
    def __init__(self, nombre, edad, dni, salario, cargo: str):
        super().__init__(nombre, edad, dni)   
        self._salario = salario
        self.cargo = cargo
        
    @property
    def dni(self):                            #Encapsulamiento   
        return self._dni
    
    @property                                 #Encapsulamiento
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, salario):
        self._salario = salario
    
    def mostrar_info(self):                   #Abstraccion(implementacion)
        return f"Nombre: {self.nombre} Edad: {self.edad} DNI:{self._dni} Salario: {self._salario} cargo: {self.cargo}"
    
    def consultar_salario(self):
        if self.cargo == "Administrativo":
            return f"El salario base de Administracion es de : $ {self._salario}"
        elif self.cargo  == "Gerente":
            return f"El salario base de Gerente es de: $ {self._salario}"
        elif self.cargo  == "Vendedor":
            return f"El salario base de Vendedor es de $ {self._salario}"
    
    def calcular_salario(self):
        if self.cargo == "Administrativo":
            return self._salario + (self._salario * 0.1)
        elif self.cargo == "Gerente":
            return self._salario + (self._salario * 0.3)
        elif self.cargo == "Vendedor":
            return self._salario + (self._salario * 0.2)