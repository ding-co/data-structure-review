- Circular Linked List
  - not use head variable, only use tail variable
  - At the end of node, node next link -> first node
  - advantage: can remove head variable

```python
# Circular Singly Linked List
# head, tail variable (none)

# insert_head('A')
# var(head) -> node(A, A)
# var(tail) -> node(A, A)

# insert_head('B')
# var(head) -> node(B) -> node(A, B)
# var(tail) -> node(A, B)

# insert_tail('C')
# var(head) -> node(B) -> node(A) -> node(C, B)
# var(tail) -> node(C, B)

# remove head variable
# how to find tail? => tail next is head

# how about remove tail variable and just keep head variable?
# => insert_tail impossible (it is not a doubly linked list)

# doubly linked list - Good
# Circular singly linked list (tail) - Good
```

- Circular SLL (tail)

```python
# Circular SLL (tail)
class CircularSinglyLinkedList:
  class Node:
    def __init__(self, value):
      self.value = value
      self.next = None

  def __init__(self):
    self.tail = None
    self.cnt = 0

  def insert_head(self, value):
    node = self.Node(value)
    self.cnt += 1
    if not self.tail:
      # point node itself
      node.next = node
      self.tail = node
      return
    node.next = self.tail.next
    self.tail.next = node

  def insert_tail(self, value):
    node = self.Node(value)
    self.cnt += 1
    if not self.tail:
      node.next = node
      self.tail = node
      return
    node.next = self.tail.next
    self.tail.next = node
    self.tail = node

  def delete_head(self):
    if not self.tail:
      return
    self.cnt -= 1
    # node numbers => only one
    if self.tail == self.tail.next:
      self.tail = None
      return
    # node numbers => greater than or equal to 2
    self.tail.next = self.tail.next.next

  def delete_tail(self):
    # ** To Do: Implementation **
    return

  def count(self):
    return self.cnt

  def print_all(self):
    if not self.tail:
      return
    head = self.tail.next
    p = head
    while p:
      print(p.value, end = " ")
      p = p.next
      if p == head:
        break
    print()

# Simple test case
cirSll = CircularSinglyLinkedList()
cirSll.insert_head('A')
cirSll.insert_head('B')
cirSll.insert_tail('C')
cirSll.insert_tail('D')
cirSll.print_all()
# cirSll.delete_tail()
# cirSll.print_all()
cirSll.delete_head()
cirSll.print_all()
```
