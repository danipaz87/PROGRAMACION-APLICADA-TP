"""Libro: Crear las clases Libro y Libreria. La clase Libro debe incluir atributos como titulo, autor y precio.
La clase Libreria debe contener una lista de objetos Libro y métodos para calcular el precio total de todos
los libros en la librería"""


class Libro:
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
        
    def agregarlibros(self):
        pass
    
    def calcular_pciototal(self):
        pass
        
class Libreria:
    def __init__(self):
        self.libros = []
    
    def agregalibros(self, libro):
        self.libros.append(libro)
        
        
    def calcular_pciototal(self):
        total=0
        for libro in self.libros:
            total += libro.precio
        return total
    

    
libro1= Libro("Harry Potter y La Piedra Filosofal" , "J. K. Rowling", 15000 )
libro2= Libro("Harry Potter y La Camara Secreta" , "J. K. Rowling", 17000 )
libro3= Libro("Harry Potter y Las Reliquias de la Muerte" , "J. K. Rowling", 20000 )

libreria = Libreria()
libreria.agregalibros(libro1)
libreria.agregalibros(libro2)
libreria.agregalibros(libro3)



print("El precio de los libros es de : ", libreria.calcular_pciototal())