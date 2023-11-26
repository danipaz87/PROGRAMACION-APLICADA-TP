from Libro import Libro
from Libreria import Libreria

libro1= Libro("Harry Potter y La Piedra Filosofal" , "J. K. Rowling", 15000 )
libro2= Libro("Harry Potter y La Camara Secreta" , "J. K. Rowling", 17000 )
libro3= Libro("Harry Potter y Las Reliquias de la Muerte" , "J. K. Rowling", 20000 )

libreria = Libreria()
libreria.agregalibros(libro1)
libreria.agregalibros(libro2)
libreria.agregalibros(libro3)

print("Libros:\n",libreria.listar_libros())

print("El precio total de los libros es de : ", libreria.calcular_pciototal())