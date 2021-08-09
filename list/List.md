## [List]

- list; something listed
- it has an order <br/>
  ex) To Do list, ceremony order

### _List vs Set_

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
  insert_head, insert_tail, delete_head, delete_tailm insert(i, x), delete(i, x)

### _List implementation using Array_

- Array
- A variable is simply a pointer to a position
- Array <br/>
  advantage: Index allows you to view any location immediately (using byte size) <br/>
  disadvantage: Difficult to dynamically scale

```python
# ex) list: a b c d e f g - -
#     cnt = 7

# list.get(Third) => return list[2] (index: 2) => c
# Time Complexity: O(1)

# insert_tail('z') => list[7] = 'z', cnt = 8
# Time Complexity: O(1)

# insert_head('h') => list[0] = 'h',cnt = 9
# The remaining elements should be moved to the right one space. (right-shifted by one)
# Time Complexity: O(n), if we put n elements => O(n^2)

# delete_tail => cnt = 8
# Time Complexity: O(1)

# delete_head => cnt = 7
# The remaining elements should be moved to the left one space. (left-shifted by one)
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
# List: node(head) -> node(B) -> node(A, none)
# insert_head => Time Complexity: O(1)

# insert_tail('C')
# insert_tail('D')
# List: node(head) -> node(B) -> node(A) -> node(C) -> node (D, none)
# insert_tail => Time Complexity: O(n)

# delete_head
# List: node(head) -> node(A) -> node(C) -> node(D, none)
# delete head => Time Complexity: O(1)

# delete_tail
# List: node(head) -> node(A) -> node(C, none)
# delete_tail => Time Complexity: O(n)

# if we declare a variable that point the tail?

# insert_head('A')
# List: node(head) -> node(A, none)
#       node(tail) -> node(A, none)

# insert_head('B')
# List: node(head) -> node(B) -> node(A, none)
#       node(tail) -> node(A, none)
# insert_head => Time Complexity: O(1)

# insert_tail('C')
# List: node(head) -> node(B) -> node(A) -> node(C, none)
#       node(tail) -> node(C, none)
# insert_tail => Time Complexity: O(1)

# get_tail(), get_head() => O(1)

# get(n) => O(n)

# delete_head => O(1)

# delete_tail => O(n)
# we don't know in front of the tail item

# Another idea ?? => Double Linked List!
```

- Doubly Linked List

- Circular Linked List

#

## [Note]

- ADT
- iterate
- array != list
- The list has an order, so the existing order must be maintained
- Array must be pre-sized
- link (pointer); has the address of next item
- data item (node)
- if link disconnect => become like an Interstellar lost child
- python; if anything reference something, something will be disappeared (dangling)
