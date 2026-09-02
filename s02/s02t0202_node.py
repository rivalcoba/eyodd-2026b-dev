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
