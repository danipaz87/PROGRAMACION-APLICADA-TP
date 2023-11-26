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
    
    def listar_libros(self):
        return f"Titulo: {self.titulo} - Autor: {self.autor} - Precio: $ {self.precio} \n"
    
    def calcular_pciototal(self):
        pass
    