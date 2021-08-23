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
