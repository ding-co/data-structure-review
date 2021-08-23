### _Linked List_

- Singly Linked List

  - Add link to the end of item (pointer, point next item)
  - it has a variable that point head
  - advantage: need not to be pre-sized

```python
# insert_head('A')
# insert_head('B')
# List: var(head) -> node(B) -> node(A, none)
# insert_head => Time Complexity: O(1)

# insert_tail('C')
# insert_tail('D')
# List: var(head) -> node(B) -> node(A) -> node(C) -> node (D, none)
# insert_tail => Time Complexity: O(n)

# delete_head
# List: var(head) -> node(A) -> node(C) -> node(D, none)
# delete head => Time Complexity: O(1)

# delete_tail
# List: var(head) -> node(A) -> node(C, none)
# delete_tail => Time Complexity: O(n)

# if we declare a variable that point the tail?

# insert_head('A')
# List: var(head) -> node(A, none)
#       var(tail) -> node(A, none)

# insert_head('B')
# List: var(head) -> node(B) -> node(A, none)
#       var(tail) -> node(A, none)
# insert_head => Time Complexity: O(1)

# insert_tail('C')
# List: var(head) -> node(B) -> node(A) -> node(C, none)
#       var(tail) -> node(C, none)
# insert_tail => Time Complexity: O(1)

# get_tail(), get_head() => O(1)

# get(nth) => O(n)

# delete_head => O(1)

# delete_tail => O(n)
# we don't know before tail item

# Another idea ?? => Double Linked List!
```

- SLL (head)

```python
# SLL (head)
class SinglyLinkedList1:
  class Node:
    def __init__(self, value):
      self.value = value
      self.next = None

  def __init__(self):
    self.head = None
    # it can declare new variable - cnt
    # memory cost up, time cost down, consistency low
    # self.cnt = 0

  # Time Complexity: O(1)
  def insert_head(self, value):
    node = self.Node(value)
    # if not self.head: node.next = None
    # if self.head: node.next = previous_head
    node.next = self.head
    self.head = node
    # self.cnt += 1

  # Time Complexity: O(n)
  def insert_tail(self, value):
    node = self.Node(value)
    if not self.head:
      self.head = node
      return
    # p: present node
    p = self.head
    while p.next:
      p = p.next
    # p: tail
    p.next = node
    # p will be disappeared when method call end (local variable)
    # self.cnt += 1

  # Time Complexity: O(1)
  def delete_head(self):
    if not self.head:
      return
    self.head = self.head.next
    # previous_head will be disappeared (Garbage Collector)
    # self.cnt -= 1

  # Time Complexity: O(n)
  def delete_tail(self):
    if not self.head:
      return
    curr = self.head
    prev = None
    while curr.next:
      prev = curr
      curr = curr.next
    # prev: before tail
    if prev:
      prev.next = None
    else:
      self.head = None
    # self.cnt -= 1

  # if not pre-count, Time Complexity: O(n)
  def count(self):
    cnt = 0
    p = self.head
    while p:
      cnt += 1
      p = p.next
    return cnt
    # return self.cnt

  # Time Complexity: O(n)
  def print_all(self):
    p = self.head
    while p:
      print(p.value, end = " ")
      p = p.next
    print()

# Simple test case
sll = SinglyLinkedList1()
sll.insert_head('A')
sll.insert_head('B')
sll.insert_tail('C')
sll.insert_tail('D')
sll.print_all()
sll.delete_tail()
sll.print_all()
sll.delete_head()
sll.print_all()
```

- SLL (head, tail)

```python
# SLL (head, tail)
class SinglyLinkedList2:
  class Node:
    def __init__(self, value):
      self.value = value
      self.next = None

  def __init__(self):
    self.head = None
    self.tail = None
    self.cnt = 0

  def insert_head(self, value):
    node = self.Node(value)
    self.cnt += 1
    if not self.head:
      self.head = node
      self.tail = node
      return
    node.next = self.head
    self.head = node

  def insert_tail(self, value):
    node = self.Node(value)
    self.cnt += 1
    if not self.head:
      self.head = node
      self.tail = node
      return
    self.tail.next = node
    self.tail = node

  def delete_head(self):
    if not self.head:
      self.tail = None
      return
    self.head = self.head.next
    self.cnt -= 1

  def delete_tail(self):
    if not self.head:
      self.tail = None
      return
    current = self.head
    prev = None
    while current.next:
      prev = current
      current = current.next
    if prev:
      prev.next = None
      self.tail = prev
    else:
      self.head = None
      self.tail = None
    self.cnt -= 1

  def count(self):
    return self.cnt

  def print_all(self):
    p = self.head
    while p:
      print(p.value, end = " ")
      p = p.next
    print()

# Simple test case
sll = SinglyLinkedList2()
sll.insert_head('A')
sll.insert_head('B')
sll.insert_tail('C')
sll.insert_tail('D')
sll.print_all()
sll.delete_tail()
sll.print_all()
sll.delete_head()
sll.print_all()
```
