from Forma import Forma


class Rectangulo(Forma):
    def __init__(self, color, base , altura):
        super().__init__(color, dimensiones ={"base": base , "altura": altura})
        
    def calcular_area(self):
        return (self.dimensiones["base"] * self.dimensiones["altura"])
    
    def calcular_perimentro(self):
        return 2 * (self.dimensiones["base"] + self.dimensiones["altura"])