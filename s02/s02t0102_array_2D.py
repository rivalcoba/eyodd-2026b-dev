# Arreglo 2D usando listas
from array import *
table = [
  array('i',[1,2,3]),
  array('i',[4,5,6]),
  array('i',[7,8,9])
]

# Eliminando una fila
del table[1]

for r in table:
  for c in r:
    print(c, end = " ")
  print()