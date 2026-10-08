# Creando la clase
class Stack:
  def __init__(self):
    # Inicializando la pila como una lista vacía
    self.stack = []

  def size(self):
    # Retornando el tamaño de la pila
    return len(self.stack)
  
  def clear(self):
    # Vaciando la pila
    self.stack.clear()
  
  def push(self, value):
    # Agregando un elemento a la pila
    self.stack.append(value)

  def pop(self):
    # Eliminando y retornando el elemento superior de la pila
    if not self.is_empty():
      return self.stack.pop()
    else:
      return None

  def peek(self):
    # Viendo el elemento superior de la pila sin eliminarlo
    if not self.is_empty():
      return self.stack[-1]
    else:
      return None
    
  def is_empty(self):
    # Verificando si la pila está vacía
    return self.size() == 0
  # Print stack
  def print_stack(self):
    # Imprimiendo la pila
    print(self.stack)

# ---------------------
# Probando el stack
stack = Stack()
print(stack.is_empty())  # True
stack.push(1)
stack.push(10)
stack.push(30)
stack.push(2)
stack.push("1")
stack.print_stack() # [1, 10, 30, 2, '1']
print(stack.peek())      # 2
print(stack.pop())       # 2
print(stack.size())      # 3
stack.clear()
print(stack.is_empty())  # True
