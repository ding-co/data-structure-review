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
- Garbage Collection; remove not using something
