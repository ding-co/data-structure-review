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

# declare 2 variables => front, rear
# let, front = 0, rear = 0
# if add: front++, if delete: return current rear and then rear++
# add: O(1), delete: O(1)
# problem: when we delete an element, we can't use before memory spaces
# array's space has set at first time (it's hard to stretch in the middle)
# if we use all of memory's space, and then go to the first index of the array => O(n)
# how can we solve above problem??

# Use Circular Queue!!!
```

- Implementation Queue with LinkedList

```python
# CirSLL(t)
# Q.add => insert_tail()
# Q.delete => delete_head()

# DLL
# can use either one (b/c it has two links)
# case 1: Q.add / Q.delete => insert_head() / delete_tail()
# case 2: Q.add / Q.delete => insert_tail() / delete_head()
```

- Deque (Double-Ended Queue)

```python
# Queue (FIFO)
# make it more general
# add -> delete ->
# <- delete <- add

# front - rear
# we can add front / add rear
# we can delete rear / delete front

# we can make Stack, Queue with Deque

# 4 functions
# AddFront
# AddRear
# DeleteFront
# DeleteRear

# if we add front and delete front => Stack

# we may can make Deque with array
# => make it circular bi-direction

# we can make Deque with DLL!!!
# => insert_head(), delete_head(), insert_tail(), delete_tail()

# Queue in Python (using DLL)
# collections package (deque)
# append, appendleft, pop, popleft

# queue.Queue - A synchronized queue class
# asyncio.Queue - asyncio queue API
# it has already implemented in Python modules...
```

- Utilization

  - Stack

    - OS/Memory
    - Function call
    - Stack Memory

  - Queue

    - line up (waiting list)
      - bank waiting (fair)
    - Job Scheduling
    - Network Transport
    - File I/O
    - Distributed Computing
    - Keyboard Typing
      - Queue(Worker) - Processor
      - Program lined in queue without dying
    - Event Queue
    - types

      - Deque
      - Priority Queue

        - ex) Emergency room
        - it must be served first...
        - Each patient has a priority

      - Sync, Async
        - Sync; You have to wait in the queue until you're done. (spend more time for waiting)
        - Async; call my name that I will stand in line.
          - When we add to the queue, we wait until the result is over and then delete it.
          - if multiple programs add to one queue at the same time. <br/>
            => it can be crashed. (not ensure reliability) <br/>
            => we have to make some protection for parallel process. <br/>
          - we have to make good code for concurrent control <br/>
            (multiple processes/threads access at the same time => may crashed) <br/>
            => We can use a Number table (ensure each order)
      - Big data; Queue => Clustering

#

## [Note]

- Stack; push, pop (LIFO)
- delete memory is not correct concept
