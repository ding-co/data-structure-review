## [List]

- list; something listed
- it has an order <br/>
  ex) To Do list, ceremony order, ...

### _List vs. Set_

- common: a collection of things (Data collection structure)
- difference <br/>
  List: Order O, Overlap O <br/>
  Set: Order X, Overlap X

### _List work_

- data +: insert / add
- data -: delete / remove
- data lookup: read / get
- is_empty?
- count?
- where? front / rear / between <br/>
  insert_head, insert_tail, delete_head, delete_tail, insert(i, x), delete(i, x)

### _List implementation using Array_

- A variable is simply a pointer to a position
- Array <br/>
  advantage: Index allows you to view any location immediately (using byte size) <br/>
  disadvantage: Difficult to dynamically scale

```python
# ex) list: a b c d e f g none none
#     cnt = 7

# list.get(Third) => return list[2] (index: 2) => c
# Time Complexity: O(1)

# insert_tail('z') => list[7] = 'z', cnt = 8
# Time Complexity: O(1)

# insert_head('h') => list[0] = 'h',cnt = 9
# The remaining elements should be moved to the right one space (right-shifted by one)
# Time Complexity: O(n), if we put n elements => O(n^2)

# delete_tail => cnt = 8
# Time Complexity: O(1)

# delete_head => cnt = 7
# The remaining elements should be moved to the left one space (left-shifted by one)
# Time Complexity: O(n)

# tail - good, get - good
# head - bad
```

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

- Doubly Linked List

  - two links (before, next)

```python
# insert_head('A')
# List: var(head) -> node(none, A, none)
#       var(tail) -> node(none, A, none)

# insert_head('B')
# List: var(head) -> node(none, B) <-> node(A, none)
#       var(tail) -> node(A,none)

# insert_tail('C')
# List: var(head) -> node(none, B) <-> node(A) <-> node(C, none)
#       var(tail) -> node(C, none)

# insert_tail('D')
# List: var(head) -> node(none, B) <-> node(A) <-> node(C) <-> node(D, none)
#       var(tail) -> node(D, none)

# insert_head, insert_tail => O(1)

# delete_head => O(1)

# delete_tail
# List: var(head) -> node(none, B) <-> node(A) <-> node(C, none)
#       var(tail) -> node(C, none)

# delete_tail => O(1)

# get(nth) => O(n)

# head, tail two variables => too many code lines (ex. if statement)
# => declare a variable that points empty head node
# => var(head) -> head_node(self, none, self)

# insert_head('A') => head next 'A'
# var(head) -> head_node(none) <-> node(A)
#              node(A) <-> head_node(none)

# insert_head('B') => head next 'B'
# var(head) -> head_node(none) <-> node(B) <-> node(A)
#              node(A) <-> head_node(none)

# insert_tail('C') => head before 'C'
```

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

# Circular doubly linked list - Good
# Circular singly linked list (tail) - Good
```

- Array vs. Linked List <br/>
  (Let, array size enough, not overflow <br/>
  insert(nth), delete(nth) suggest pre-find node)

|        Comparison        | Array |  SLL(h)   | SLL(h,t)  |    DLL    |
| :----------------------: | :---: | :-------: | :-------: | :-------: |
|         get(nth)         | O(1)  |   O(n)    |   O(n)    |   O(n)    |
|       insert_head        | O(n)  |   O(1)    |   O(1)    |   O(1)    |
|       insert_tail        | O(1)  |   O(n)    |   O(1)    |   O(1)    |
|       delete_head        | O(n)  |   O(1)    |   O(1)    |   O(1)    |
|       delete_tail        | O(1)  |   O(n)    |   O(n)    |   O(1)    |
| insert(i, x)/find before | O(n)  | O(1)/O(n) | O(1)/O(n) | O(1)/O(1) |
|       delete(i, x)       | O(n)  |   O(n)    |   O(n)    |   O(1)    |

- Space complexity <br/>
  Array: O(n), <br/>
  SLL(h): O(2n)? [b/c link] => O(n) <br/>
  DLL: O(3n)? => O(n)

## List Implementation

- Array

```python
class Array:
  def __init__(self):
    self.data = [None] * 100
    self.cnt = 0

  def insert_head(self, value):
    for i in range(self.cnt, 0, -1):
      self.data[i] = self.data[i - 1]
    self.data[0] = value
    self.cnt += 1

  def insert_tail(self, value):
    self.data[self.cnt] = value
    self.cnt += 1

  def delete_head(self):
    for i in range(self.cnt):
      self.data[i] = self.data[i + 1]
    self.cnt -= 1

  def delete_tail(self):
    # self.data.pop()
    self.cnt -= 1

  def count(self):
    return self.cnt

  def print_all(self):
    for i in range(self.cnt):
      print(self.data[i], end = " ")
    print()

# Simple test case
array = Array()
array.insert_head('A')
array.insert_head('B')
array.insert_tail('C')
array.insert_tail('D')
array.print_all()
array.delete_tail()
array.print_all()
array.delete_head()
array.print_all()
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

- Circular DLL (head, empty head node)

```python

```

#

## [Note]

- ADT
- iterate
- array != list
- The list has an order, so the existing order must be maintained
- Array must be pre-sized
- link (pointer); has the address of next item
- data item (node)
- if link disconnects => become like an Interstellar lost child
- python; if anything reference something, something will be disappeared (dangling)
- Garbage Collection; remove not using something <br/>
  (anything that references something, something will be dangled)
- module; black box (encapsulation)
- Always thinking about what function outside <br/>
  rather than inside implementation
- class; reference address
- C language; delete garbage explicitly with code
-
