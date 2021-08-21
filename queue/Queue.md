## [Queue]

### _Queue_

- Standing in line <br/>
  ex) bank
- FIFO (First In First Out)
- ADT (Abstract Data Type)
  - a kind of list
  - add, delete
  - isFull, isEmpty
- implementation;
  - Stack X (may be hard b/c a completely different properties)
  - Array? OK
  - LinkedList OK
    - SLL(h), SLL(h,t), CirSLL(t)
    - DLL
      |option|Queue.add|Queue.delete|DLL|SLL(h)|SLL(h,t)|CirSLL(t)
      |:--:|:--:|:--:|:--:|:--:|:--:|:--:|
      |1|insert_head()|delete_tail()|O(1)/O(1)|O(1)/O(n)|O(1)/O(n)|O(1)/O(n)
      |2|insert_tail()|delete_head()|O(1)/O(1)|O(n)/O(1)|O(1)/O(1)|O(1)/O(1)
    - only for queue => CirSLL(t) > SLL(h,t) > DLL (b/c DLL spend more space)
    - if, insert_head(), delete_head() => Stack
    - if, we use Linkedlist => spend space as much as we can and T.C O(1)/O(1)
    - CirSLL(t) is OK, but DLL more useful (for Deque)

<br/>

- Implementation Queue with List

```python
# 0 1 2 3 4 5 6 7 8 9 10 ... (array index)
# Q.add(A)
# Q.add(B)
# Q.add(C)
# Q.delete()
# Q.delete()
# Q.delete()

# way 1. declare 2 variables => front, rear
# let, front = 0, rear = 0
# if add: front++, if delete: rear++
# add: O(1), delete: O(1)
# problem: when we delete an element, we can't use before variables
# array's space has set at first time (it's hard to stretch in the middle)
# if we use all of memory's space, and then go to the first index of the array => O(n)
# how can we solve above problem??

# Use Circular Queue!!!
```

#

## [Note]

- Stack; push, pop (LIFO)
