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

  # Delete the first node
  def delete_first_node(self):
    if self.head is None:
      print("La lista está vacía. No se puede eliminar el primer nodo.")
      return None
    # Guardamos el dato del nodo que será eliminado para retornarlo posteriormente
    deleted_data = self.head.data
    self.head = self.head.next
    # Si la lista queda vacía después de eliminar el primer nodo, actualizamos la cola a None
    if self.head is None:
      self.tail = None
    # Actualizamos el tamaño de la lista después de eliminar el nodo
    self.size -= 1
    # Retornamos el dato del nodo eliminado
    return deleted_data
  # Delete the last node of the list
  def delete_last_node(self):
    # Si la lista está vacía, no se puede eliminar el último nodo
    if self.head is None:
      print("La lista está vacía. No se puede eliminar el último nodo.")
      return None
    # Si la lista tiene un solo nodo, eliminamos ese nodo y actualizamos head y tail a None
    if self.head.next is None:
      deleted_data = self.head.data
      self.head = None
      self.tail = None
      self.size -= 1
      return deleted_data
    # Si la lista tiene más de un nodo, recorremos hasta el penúltimo nodo
    current = self.head
    # Empezamos desde el head y avanzamos hasta encontrar el penúltimo nodo
    while current.next.next:
      current = current.next
    # current ahora apunta al penúltimo nodo
    deleted_data = current.next.data
    current.next = None
    self.tail = current
    self.size -= 1
    return deleted_data
  # Eliminando un nodo por su valor
  def delete_node_by_value(self, value):
    # Si la lista está vacía, no se puede eliminar ningún nodo
    if self.head is None:
      print("La lista está vacía. No se puede eliminar el nodo.")
      return None
    # Si el nodo a eliminar es el primer nodo
    if self.head.data == value:
      return self.delete_first_node()
    # Recorremos la lista para encontrar el nodo a eliminar
    current = self.head
    while current.next and current.next.data != value:
      current = current.next
    # Si no se encontró el nodo con el valor especificado
    if current.next is None:
      print(f"El nodo con valor {value} no se encontró.")
      return None
    # Eliminamos el nodo encontrado
    deleted_data = current.next.data
    current.next = current.next.next
    # Si el nodo eliminado era el último, actualizamos la cola
    if current.next is None:
      self.tail = current
    self.size -= 1
    return deleted_data
# ----------------- FIN DE LA CLASE -----------------

# -------------- USO ---------------------
# Creando una lista enlazada
linked_list = SinglyLinkedList()
# Agregando elementos a la lista enlazada
linked_list.append('eggs')
linked_list.append('ham')
linked_list.append('spam')
linked_list.append('bacon')

# Impresion de lista
print("\nBefore Insertion\n")
linked_list.print_list()

# Eliminando el primer nodo
linked_list.delete_node_by_value('eggs')

# Impresion de lista
print("\nAfter Deletion\n")
linked_list.print_list()