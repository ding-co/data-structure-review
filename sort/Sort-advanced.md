## [Sort advanced]

### _Heap Sort_

- Naive way

  - heap array
  - make it to Min Heap/Max Heap
  - and then, pop() and save to a new array
  - B/A/W => T.C: O(nlog n), S.C: O(n)
    - T.C: Insert O(nlog n), Pop O(nlog n)
  - how about insert from the end of array? <br/>
    => we don't need a new array, we can just use an original array!

- Better way

  ```python
  # example
  # 0 1 2 3 4 5 (index)
  # 9 2 5 7 1 3

  # ascending order using heap sort
  # Max Heap => insert from the end of an array

  # idea
  # 1. (0 ~ n-1) up_heap (n times)
  # 2. n times - pop (swap root <-> end), down_heap
  # => T.C: O(2nlog n) => O (nlog n)
  # S.C: O(1)

  # idea 1.
  # Step 1: 9
  # Step 2: 9 2 (up_heap)
  # Step 3: 9 2 5 (up_heap every step)
  # Step 4: 9 7 5 2
  # ... => 9 7 5 2 1 3

  # idea 2.
  # 3 7 5 2 1 9 (heap is until 1)
  # 7 3 5 2 1 9
  # 1 3 5 2 7 9 (heap is until 2)
  # 5 3 1 2 7 9
  # 2 3 1 5 7 9 (heap is until 1)
  # 3 2 1 5 7 9
  # 1 2 3 5 7 9 (heap is until 2)
  # 2 1 3 5 7 9
  # 1 2 3 5 7 9 (heap is until 1)
  ```

### _Quick Sort_

- recursive algorithm
- split to pivot (standard)
- each group => recursive split to pivot (until 1 element)
- finally, all elements are sorted
- T.C: Best/Average Case => O(nlog n), Worst Case => O(n^2), not separated to half <br/>
  use 2 arrays (element < pivot, element > pivot) => S.C: O(n)
- if sorted array => worst case
- how to reduce space??
  - just use one original array! (possible)
- issue
  1. pivot?
     - random, choose of three, ...
  2. use original one array
  3. recursive call
     - quick sort recursive (partitioning)
     - call stack => O(log n) need.. (S.C => not real O(n), Best/Average Case) <br/>
       (Worst case S.C => O(n))
     - how about least elements sorting?
     - if least elements => insertion sort is good, not quick sort

```python
# example
# 0 1 2 3 4 5 6 7 8 (index)
# 5 2 7 9 1 3 8 6 4

# 0. pivot swap; candidate: 5, 1, 4; 5 <-> 4 (choose middle element)
# 4 2 7 9 1 3 8 6 5

# 1. pivot - 4 (choose front)
# 2. partitioning

# way 1. set two pointer (index); -> <-
# T.C: O(n), height: O(log n) => O(nlog n)
# first pointer: start at index 1 (point smaller than pivot)
# second pointer: start at index 8 (point bigger than pivot)

# 4 2 3 9 1 7 8 6 5
# 4 2 3 1 9 7 8 6 5
# 1 2 3 4 9 7 8 6 5

# quick_sort(arr, 0, 2)
# quick_sort(arr, 4, 8)

# quick_sort(arr, 4, 8)
# 4 5 6 7 8 (idx)
# 9 7 8 6 5 (9 <-> 8)
# 8 7 9 6 5

# way 2. declare pivot position variable; ->
# T.C: O(n), height: O(log n) => O(nlog n)
# idx = 5 (if meet smaller than pivot, save to this idx variable)
# idx = 6

# 8 7 6 9 5
# idx = 7
# 8 7 6 5 9
# idx = 8
# (idx - 1) position is before smallest number

# 5 6 7 8 9 (8 <-> 5)
```

### _Merge Sort_

### _Radix Sort_

#

### [Note]

- Selection/Insertion/Bubble Sort => T.C: O(n^2)
- [visualgo](https://visualgo.net)
