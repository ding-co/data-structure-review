class Stack:
  def __init__(self):
    self.items = []
  
  def push(self, item):
    self.items.append(item)
  
  def pop(self):
    if self.items:
      return self.items.pop()
  
  def is_empty(self):
    return not self.items

  def peek(self):
    if self.items:
      return self.items[-1]