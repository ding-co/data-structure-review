## [Max Heap]

### _Implementation_

- parent is a captain (largest number)
- pop => sort descending

```python
# Max Heap
class MaxHeap:
  def __init__(self):
    self.array = []

  def push(self, value):
    self.array.append(value)
    self.__up_heap(len(self.array) - 1)

  def pop(self):
    result = self.array[0]
    value = self.array.pop()
    if len(self.array) > 0:
      self.array[0] = value
      self.__down_heap(0)
    return result

  def is_empty(self):
    return len(self.array) == 0

  # private function (__)
  def __parent_idx(self, idx):
    # 0 --> 1, 2
    # 1 --> 3, 4
    # 2 --> 5, 6
    # 3 --> 7, 8
    return int((idx + 1) / 2) - 1

  def __left_idx(self, idx):
    return 2 * idx + 1

  def __right_idx(self, idx):
    return 2 * idx + 2

  def __up_heap(self, current):
    parent = self.__parent_idx(current)
    while current > 0 and self.array[current] > self.array[parent]:
      self.array[current], self.array[parent] = self.array[parent], self.array[current]
      current = parent
      parent = self.__parent_idx(current)

  def __down_heap(self, current):
    left, right = self.__left_idx(current), self.__right_idx(current)
    # child exists
    while left < len(self.array):
      # left child only exists or compare
      if right >= len(self.array) or self.array[left] > self.array[right]:
        child = left
      else:
        child = right
      if self.array[current] >= self.array[child]:
        return
      self.array[current], self.array[child] = self.array[child], self.array[current]
      current = child
      left, right = self.__left_idx(current), self.__right_idx(current)
  def print(self):
    print(self.array)
# Simple test case
heap = MaxHeap()
heap.push(5)
heap.push(10)
heap.push(3)
heap.push(8)
heap.push(13)
heap.push(27)
heap.push(4)
while not heap.is_empty():
  print(heap.pop())
```

## [Note]

- Use debugger
- unit test
