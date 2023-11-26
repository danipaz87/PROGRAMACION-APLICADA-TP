from Libro import Libro

class Libreria:
    def __init__(self):
        self.libros = []
    
    def agregalibros(self, libro):
        self.libros.append(libro)
        
    def listar_libros(self):
        listado = ""
        for libro in self.libros:
            listado += libro.listar_libros()
        return listado
        
    def calcular_pciototal(self):
        total=0
        for libro in self.libros:
            total += libro.precio
        return total
    
