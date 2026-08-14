class Node:
  def __init__(self, data = None):
    self.data = data
    self.next = None

# Creando nodos
n1 = Node('eggs')
n2 = Node('ham')
n3 = Node('spam')

# Enlazando nodos
n1.next = n2
n2.next = n3

# Link Traversal
current = n1
while current:
  print(current.data)
  current = current.next