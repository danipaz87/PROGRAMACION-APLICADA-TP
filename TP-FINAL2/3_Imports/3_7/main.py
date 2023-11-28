"""Crear dos módulos en el mismo directorio. Desde un módulo, importa una función o variable del otro utilizando una importación 
relativa y utilizar un alias"""

from pack.modulo1 import arrancar as auto_arranca
from pack.modulo2 import frenar as auto_frena

print(auto_arranca())
print(auto_frena())