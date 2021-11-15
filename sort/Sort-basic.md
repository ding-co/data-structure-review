## [Sort basic]

### _Sort_

- Sorting order: Ascending / Descending
- Key: values used to sort
  - ex) book <br/>
    (title, number, book classification code, ...) <- key candidates for sort
- sort types
  - internal sort; sorting inside memory (main memory)
  - external sort; sorting with external storage (HDD)
- sort stability
  - ex 1) 1 diamond, 2 clover, 3 spade, 2 heart (4 cards) <br/>
    (clover is before heart) <br/>
    if ascending order => 1 diamond, 2, 2, 3 spade <br/>
    if front 2 is heart and after is clover => unstable <br/>
    -> it breaks original position
  - ex 2) aa Univ. 18 John, bb Univ. 18 Ann, ... (10000 students) <br/>
    if I want to sort with Univ, StdId, name (ascending order) <br/>
    I can use all three at once to sort them out but it's too hard <br/>
    => if we have a stable algorithm, name -> StdId -> Univ (sorting order) <br/>
    (stable algorithm; keep each sorting stage)

### _Sort way_

- Card game

  - when I play the card game, I sort the card on my hands
  - ascending order

    1. find the smallest card and locate to first position (selection sort)

       - how to find the smallest card?
         - one array, declare a variable <br/>
           (select smaller card index for each comparison)

       |  Selection Sort  | worst case | best case | average case |
       | :--------------: | :--------: | :-------: | :----------: |
       | time complexity  |   O(n^2)   |  O(n^2)   |    O(n^2)    |
       | space complexity |    O(1)    |   O(1)    |     O(1)     |

    2. library; Put the book on the shelf and arrange it right away (Insertion sort)

       - Insertion Sort 1
       - Insert from one array to another array <br/>
         (use two arrays)
       - Compare every insert and sort
       - Compare numbers from the beginning

       | Insertion Sort 1 | worst case | best case | average case |
       | :--------------: | :--------: | :-------: | :----------: |
       | time complexity  |   O(n^2)   |  O(n^2)   |    O(n^2)    |
       | space complexity |    O(n)    |   O(n)    |     O(n)     |

       - Insertion Sort 2
       - use one array, 1 variable
       - Assume you've got one
       - every compare, and swap
       - Compare numbers from the beginning
       - whe have to shift rest numbers
       - compare 1, shift n <br/>
         compare n, shift 0 <br/>
         each 1 card => operation: n

       | Insertion Sort 2 | worst case | best case | average case |
       | :--------------: | :--------: | :-------: | :----------: |
       | time complexity  |   O(n^2)   |  O(n^2)   |    O(n^2)    |
       | space complexity |    O(1)    |   O(1)    |     O(1)     |

       - Insertion Sort 3
       - use one array, 1 variable
       - Compare numbers from the end
       - we don't have to shift rest numbers
       - reversed case => worst case <br/>
         pre-sorted case => best case (only read)

       | Insertion Sort 3 | worst case | best case | average case |
       | :--------------: | :--------: | :-------: | :----------: |
       | time complexity  |   O(n^2)   |   O(n)    |    O(n^2)    |
       | space complexity |    O(1)    |   O(1)    |     O(1)     |

    3. bubble sort

       - only compare next to number (every compare two numbers)
       - worst case; compare n-1 / swap n-1 (\* n)
       - base case; compare n-1 / swap 0 (\* n)

       |   Bubble Sort    | worst case | best case | average case |
       | :--------------: | :--------: | :-------: | :----------: |
       | time complexity  |   O(n^2)   |  O(n^2)   |    O(n^2)    |
       | space complexity |    O(1)    |   O(1)    |     O(1)     |

- insertion sort (reversed direction) is good <br/>
  among above naive/easy 3 sort ways.

<br/>

### _Implementation_

- sort.py

```python
# bubble sort
def bubble_sort(data):
  n = len(data)
  for i in range(n - 1, 0, -1):
    for j in range(0, i):
      if data[j] > data[j + 1]:
        data[j], data[j + 1] = data[j + 1], data[j]
  return data
```

```python
# selection sort
def selection_sort(data):
  n = len(data)
  for i in range(0, n):
    smallest_idx = i
    for j in range(i + 1, n):
      if data[smallest_idx] > data[j]:
        smallest_idx = j
    data[smallest_idx], data[i] = data[i], data[smallest_idx]
  return data
```

```python
# insertion sort
def insertion_sort(data):
  n = len(data)
  for i in range(0, n):
    # imagine on hands
    val = data[i]
    j = i
    while j > 0 and data[j - 1] > val:
      data[j] = data[j - 1]
      j -= 1
    data[j] = val
  return data
```

### _Unit Test_

- test_sort.py

```python
# bubble sort unit test
import unittest
import random
import copy
from sort_basic import bubble_sort

class TestSort(unittest.TestCase):
  def test_bubblesort(self):
    data = [5, 9, 6, 1, 2, 3, 7]
    self.assertEqual([1, 2, 3, 5, 6, 7, 9], bubble_sort(data))
    self.assertEqual([], bubble_sort([]))

  def test_bubblesort_big(self):
    data = list(range(100))
    self.assertEqual(data, bubble_sort(data))
    data = list(range(100, 0, -1))
    answer = list(range(1, 101))
    self.assertEqual(answer, bubble_sort(data))

  def test_random(self):
    for _ in range(10):
      data1 = random.sample(range(1, 100), 30)
      data2 = copy.deepcopy(data1)
      data1.sort()
      bubble_sort(data2)
      self.assertEqual(data1, data2)

if __name__ == '__main__':
  unittest.main()
```

### [Note]

- sort example 1) <br/>
  sort 5 number cards [5, 2, 7, 1, 9]
  - Ascending order
    - [1, 2, 5, 7, 9]
  - Descending order
    - [9, 7, 5, 2, 1]
  - how to instruct to computer?
- I need to be able to split up what I can do (think) <br/>
  => and then I can code with computer
- Shell Sort; insertion sort improvement
- Merge Sort/Quick Sort/Heap Sort
- Radix Sort/Counting Sort
- Recommendation: Insertion/Shell/Merge/Quick/Heap Sort
- python sort - `array.sort()`
- sort; always think the end part
- unit test; automatically performed test code <br/>
  - unittest module's TestCase inheritance
  - automatically performed method
  - assertion; if not true => error
  - It's good to pre-create unit test what I want to code
- VS Code Debugger;
