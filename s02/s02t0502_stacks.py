# Implementacion de Stack con singlylink list
from s02t0202_node import Node

class Stack:
  def __init__(self):
    # Inicializa la pila como vacía
    self.top = None
    # Inicializa el tamaño de la pila como 0
    self._size = 0

  # Verificando si esta vacio el stack
  def is_empty(self):
    return self.top is None

  # Agrega un elemento a la pila
  def push(self, value):
    new_node = Node(value)
    new_node.next = self.top
    self.top = new_node
    self._size += 1

  # Elimina y retorna el elemento superior de la pila
  def pop(self):
    if self.is_empty():
      return None
    popped_value = self.top.data
    self.top = self.top.next
    self._size -= 1
    return popped_value

  # Retorna el elemento superior de la pila sin eliminarlo
  def peek(self):
    if self.is_empty():
      return None
    return self.top.data

  # Vacía la pila
  def clear(self):
    self.top = None
    self._size = 0

  # Retorna el tamaño de la pila
  def size(self):
    return self._size

  # Imprime la pila
  def print_stack(self):
    current = self.top
    stack_values = []
    while current:
      stack_values.append(current.data)
      current = current.next
    print(stack_values)

# Probando la pila
if __name__ == "__main__":
  stack = Stack()
  stack.push(1)
  stack.push(2)
  stack.push(3)
  stack.print_stack()  # Output: [3, 2, 1]
  print(stack.pop())   # Output: 3
  print(stack.peek())  # Output: 2
  print(stack.size())  # Output: 2
  stack.clear()
  print(stack.is_empty())  # Output: True