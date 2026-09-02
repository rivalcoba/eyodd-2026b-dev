from s02t0202_node import Node

class SinglyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def append_at_a_location(self, data, index):
    if index < 1:
      print("Index must be greater than 0")
      return

    new_node = Node(data)

    # Insertar al inicio
    if index == 1:
      new_node.next = self.head
      self.head = new_node
      if self.tail is None:
        self.tail = new_node
      self.size += 1
      return

    # Recorrer la lista hasta la posición indicada
    current = self.head
    prev = None
    position = 1

    while current and position < index:
      prev = current
      current = current.next
      position += 1

    # Insertar al final si el índice apunta al último lugar disponible
    if current is None:
      if prev is None:
        self.head = new_node
        self.tail = new_node
      else:
        prev.next = new_node
        self.tail = new_node
      self.size += 1
      return

    # Insertar en una posición intermedia
    new_node.next = current
    if prev is None:
      self.head = new_node
    else:
      prev.next = new_node

    if new_node.next is None:
      self.tail = new_node

    self.size += 1
    
  def append(self, data):
    # Encapsulate the data in a Node
    new_node = Node(data)
    # Verifico si la lista tiene una cola (tail) existente
    if self.tail:
      # Si hay una cola existente, enlazo el nuevo nodo al final de la lista
      self.tail.next = new_node
      # Actualizo la referencia de la cola al nuevo nodo
      self.tail = new_node
    else:
      self.head = new_node
      self.tail = new_node
    self.size += 1

# Creando una lista enlazada
linked_list = SinglyLinkedList()
# Agregando elementos a la lista enlazada
# linked_list.append('eggs')
# linked_list.append('ham')
# linked_list.append('spam')

print("\nBedoreAfter Insertion\n")

# Recorriendo
current = linked_list.head
while current:
  print(current.data)  # Imprime: eggs, ham, spam
  current = current.next

print("\nAfter Insertion\n")
# Insertando dato intermedio
linked_list.append_at_a_location('new', 0)

# Recorrienda
current = linked_list.head
while current:
  print(current.data)  # Imprime: eggs, ham, spam
  current = current.next
'''
# Link Traversal 2
for val in linked_list.head.iter():
  print(val)  # Imprime: eggs, ham, spam
'''