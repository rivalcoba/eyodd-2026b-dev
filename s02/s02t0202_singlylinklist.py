from s02t0202_node import Node

class SinglyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  # Implementación de la busqueda de datos
  def search(self, data):
    for value in self.head.iter():
      if value == data:
        return value
    return None
      
  def append_at_a_location(self, data, index):
    # Verifico si el índice está dentro del rango válido
    if index < 1 or index > self.size + 1:
      raise IndexError(
        f"Índice {index} fuera de rango. "
        f"Debe estar entre 1 y {self.size + 1}."
      )

    # Creo un nuevo nodo con el dato proporcionado
    new_node = Node(data)

    # Si el índice es 1, inserto al inicio de la lista
    if index == 1:
      new_node.next = self.head
      self.head = new_node
      if self.tail is None:
        self.tail = new_node
      self.size += 1
      return

    # Si el índice no es 1, procedemos a buscar la posición adecuada para la inserción
    # Con estas variables mantendremos
    # la posición actual durante la iteración
    current = self.head
    prev = None
    position = 1
    # Iteramos sobre la lista hasta llegar a la posición deseada
    while current is not None and position < index:
      prev = current
      current = current.next
      position += 1


    # Si llegamos al final de la lista, insertamos al final
    if current is None:
      prev.next = new_node
      self.tail = new_node
      self.size += 1
      return

    # Si llegamos a una posición intermedia, insertamos el nuevo nodo aquí
    new_node.next = current
    prev.next = new_node
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

  def print_list(self):
    current = self.head
    while current:
      print(current.data)
      current = current.next
# ----------------- FIN DE LA CLASE -----------------

# -------------- USO ---------------------
# Creando una lista enlazada
linked_list = SinglyLinkedList()
# Agregando elementos a la lista enlazada
linked_list.append('eggs')
linked_list.append('ham')
linked_list.append('spam')

# Impresion de lista
print("\nBefore Insertion\n")
linked_list.print_list()

# Insertando dato intermedio
linked_list.append_at_a_location('new', 2)

# Impresion de lista
print("\nAfter Insertion\n")
linked_list.print_list()

# Buscando elementos
data_to_search = ['new', 'eggs','neww']
for data in data_to_search:
  found_value = linked_list.search(data)
  if found_value:
    print(f"Elemento encontrado: {found_value}")
  else:
    print("Elemento no encontrado")


'''
# Link Traversal 2
for val in linked_list.head.iter():
  print(val)  # Imprime: eggs, ham, spam
'''