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
     - call stack => O(log n); Best/Average Case <br/>
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

- combine with two sorted list
- pre-sorted list (run)

```python
# example
# 3 9 2 7 6 5 1 8 0 4

# two sorted list -> push to a new array

# Stage 1
# step 1: [3], [9] merge
# => [3, 9]

# step 2: [2], [7] merge
#  => [2, 7]

# step 3: [6], [5] merge
# => [5, 6]

# step 4: [1], [8] merge
# => [1, 8]

# step 5: [0], [4] merge
# => [0, 4]

# Stage 2
# step 1: [3, 9], [2, 7] merge two runs (using two pointers)
# => [2, 3, 7, 9]

# step 2: [5, 8], [1, 8] merge
# => [1, 5, 6, 8]

# Stage 3
# step 1: [2, 3, 7, 9], [1, 5, 6, 8] merge two runs
# => [1, 2, 3, 5, 6, 7, 8, 9]

# Stage 4
# step 1: [1, 2, 3, 5, 6, 7, 8, 9], [0, 4] merge
# => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# if merge, two pointers => we can just use one loop
# we just read only n data => O(n)
# only focus to how many times that we make runs?

# n -> n/2 * 2 -> n/4 * 4 -> n/8 * 8 -> ...
# total level: O(log2 n) <- merge times (height)

# T.C: worst/best/average case => O(n log n)

# example
# merge two runs (run: pre-sorted array)
# k n-k merge => n (using two pointers)
# T.C: O(n); merge one
# S.C: O(n); we need one array more

# total T.C => O(n log n)
#       S.C => O(n)

# utilization (merge sort, external sort)
# example
# computer main-memory (RAM) => we can read only 100 data
# but we need 1000 data
# we can use merge sort (file based sort)

# we can use merge sort to Database too
# => sort big data
# => external sort very good!

# if least data => merge sort is not really so good

# hybrid sort => merge + insertion sort, ...
```

### _Shell Sort_

- insertion sort improved version

```python
# insertion sort disadvantage
# if insert data is the smallest number (aim: ascending order)
# we need n times shift & n times comparison

# shell sort
# make shift size bigger (half recursive => move)
# move times (average) => O(log n)

# T.C => O(n (log n)^2)
```

### _Radix Sort_

- special case
- ex) each digit number is selected or short <br/>
  (digit number category should be selected to each digit number)

```python
# example
# 0 ~ 9 cards (total 100 numbers)

# if 1 digit number
# ex) 3, 2, 0, 6, 2, 9, 7, 1, 5, 0
# make a queue (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# when we meet queue's number, just put item
# 0, 0, 1, 2, 2, 3, 5, 6, 7, 9 (pop each queue's index)

# if 3 digit number
# ex) 352, 47, 102, 29, 4, 507, 19
# let a queue (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# LSD (Least Significant Digit; start from the end)
# => FIFO, stable (keep original order about same numbers)

# 0
# 1
# 2 - 352, 102
# 3
# 4 - 4
# 5
# 6
# 7 - 47, 507
# 8
# 9 - 29, 19

# => step 1: 352, 102, 4, 47, 507, 29, 19 (sorted by end digit number)

# 0 - 102, 4, 507
# 1 - 19
# 2 - 29
# 3
# 4 - 47
# 5 - 352
# 6
# 7
# 8
# 9

# => step 2: 102, 04, 507, 19, 29, 47, 352 (sorted by middle digit number)

# 0 - 4, 19, 29, 47
# 1 - 102
# 2
# 3 - 352
# 4
# 5 - 507
# 6
# 7
# 8
# 9

# => step 3: 4, 19, 29, 47, 102, 352, 507 (sorted by first digit number)

# O(n + n) => O(n) for 1 digit number
# queue insert: n, queue pop: n
# ==> w digit numbers => T.C: O(n * w)

# S.C: O(n + w)
# if use linked list => queue O(n)
```

|   Sort type   |    Best     |  Average  |   Worst   | Stable |
| :-----------: | :---------: | :-------: | :-------: | :----: |
| **Insertion** |    O(n)     |  O(n^2)   |  O(n^2)   |   Y    |
|   Selection   |   O(n^2)    |  O(n^2)   |  O(n^2)   |   N    |
|    Bubble     | O(n^2)/O(n) |  O(n^2)   |  O(n^2)   |   Y    |
|     Shell     |   O(n^2)    | O(n^1.5)  | O(n^1.5)  |   Y    |
|   **Quick**   |  O(n logn)  | O(n logn) |  O(n^2)   |  N/Y   |
|   **Heap**    |  O(n logn)  | O(n logn) | O(n logn) |   N    |
|   **Merge**   |  O(n logn)  | O(n logn) | O(n logn) |   Y    |
|     Radix     |  O(d \* n)  | O(d \* n) | O(d \* n) |   Y    |

### _Real World Implementation_

- General
  - Small dataset: Insertion sort
  - Large dataset: Quick, Heap, Merge
- Hybrid
  - Timsort (by Tim Pertes 2002)
    - Merge sort + Insertion sort
    - Python, Java7
  - Introsort (by David Musser 1997)
    - Quick sort + Heap sort
    - C++, .NET

#

### [Note]

- Selection/Insertion/Bubble Sort => T.C: O(n^2)
- quick sort/insertion sort/bubble sort <br/>
  => all sort way is based on main-memory sort
- if pre-sorted array, using bubble sort => T.C: O(n) <br/>
  (just focus on how many times that each item swapped)
- [visualgo](https://visualgo.net)
