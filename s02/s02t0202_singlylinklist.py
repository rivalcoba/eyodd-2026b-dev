class Node:
  def __init__(self, data = None):
    self.data = data
    self.next = None
  
  def iter(self):
    current = self
    while current:
      val = current.data 
      current = current.next 
      yield val
      
class SinglyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def append_at_a_location(self, data, index):
    # Iniciando en el primer nodo
    current = self.head
    # No hay uno anterior
    prev = self.head
    # Creando instancia del nodo a insertar
    node = Node(data)
    count = 1
    while current:
      if count == 1:
        node.next = current
        self.head = node
        print(count)
        return
      elif index == index:
        node.next = current
        prev.next = node
        return
      count += 1
      # El nodo actual se vuelve el anterior
      prev = current
      # El actual se vuelve el siguiente
      current = current.next
    if count < index:
      print("The list has less numbers of elements")
    
  def append(self, data):
    # Encapsulate the data in a Node
    new_node = Node(data)
    # 
    if self.tail:
      self.tail.next = new_node
      self.tail = new_node
    else:
      self.head = new_node
      self.tail = new_node
    self.size += 1

# Creando una lista enlazada
linked_list = SinglyLinkedList()
# Agregando elementos a la lista enlazada
linked_list.append('eggs')
linked_list.append('ham')
linked_list.append('spam')

# Recorriendo
current = linked_list.head
while current:
  print(current.data)  # Imprime: eggs, ham, spam
  current = current.next

# Insertando dato intermedio

'''
# Link Traversal 2
for val in linked_list.head.iter():
  print(val)  # Imprime: eggs, ham, spam
'''