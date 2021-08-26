## [Priority queue]

### _ADT_

- Priority Queue black box
- Operation
  - push(q, e)
    - Add e(value) with priority to Priority Queue
    - we can push only priority b/c value can be associated with priority
  - pop()
    - returns the element with the highest priority
  - peek
    - see what's at the top

```python
# example
# priority standard: large number

# q.push(10)
# q.push(1)
# q.push(15)

# q.pop => 15
# q.pop => 10
# q.pop => 1
```

### _Implementation_

- Array?

  - way 1
    - just append elements to Array (push, O(1))
    - when pop, search the largest number and then return it (pop, O(n))
    - after, swap the end element with returned value position
  - way 2
    - use insertion sort (utilize selection sort) <br/>
      maintain sorted order every push (push, O(n))
    - and then just pop (pop, O(1))

- Linked List?

  - way 1
    - insert_head, insert_tail, insert into middle good..
    - ex) push 5, push 100, push 3, push 10, pop? (large number) <br/>
      head - 10 -> 3 -> 100 -> 5 (push: O(1), pop: O(n))
  - way 2
    - if when push, make it to sorted array <br/>
      let the largest number come to the head <br/>
      push: O(n), pop: O(1)...

- Tree?
  - way for maintaining sorted state is not a bad choice
  - Binary Search Tree?
  - We have to know a new concept! => [heap](https://github.com/ding-co/data-structure/blob/main/heap/Concept.md)

#

## [Note]

- Queue (FIFO)
- Priority Queue <br/>
  ex. emergency room patient priority, <br/>
  OS job scheduler,...
- match to each pair (words) <br/>
  insert - delete <br/>
  add - remove <br/>
  push - pop
- Usually not all-around method <br/>
  (trade-off relationship)
