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

- DLL (head, empty head node)

```python
# To Do: Implementation DLL
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
