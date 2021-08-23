## [Circular queue]

```python
# Circular Queue

# 0 1 2 3 4 (array index)
# make it circular (like 0 1 2 3 4 0 1 2 3 4 ...)
# declare 2 variables => front, rear
# let, front = 0, rear = 0
# if add: front++, if delete: return current rear and then rear++
# index: when 5 -> 0 (it has to be changed)
# how do we know Full? or Empty?
# Empty? start: F == R (0 == 0)
# Full? end: F == R ...? (ex. 2 == 2)
# how can we separate above two cases...?

# It may have many solutions.

# MAX: Maximum number of entries allowed (index + 1 b/c zero index)

# way 1. declare a count variable
# when add, then count++, delete, then count--
# if, count == 0 then Empty
# if, count == MAX then Full

# way 2. use up one less memory space
# ex) total memory spaces: 4, if front == 3 then Full
# over MAX => we have to make front to 0
# if, (front + 1) % MAX == rear then Full
# count f/r, if, f == r then empty
```

```python
class CircularQueue:
    def __init__(self, max_size):
      self.max_size = max_size + 1
      self.queue = [None] * self.max_size
      self.front = 0
      self.rear = 0

    def add_queue(self, data):
      if self.is_full():
        return None
      self.queue[self.front] = data
      self.front = (self.front + 1) % self.max_size
      return True

    def delete_queue(self):
      if self.is_empty():
        return None
      delete_data = self.queue[self.rear]
      self.rear = (self.rear + 1) % self.max_size
      return delete_data


    def is_full(self):
      return (self.front + 1) % max_size == self.rear

    def is_empty(self):
      return self.front == self.rear

    def size(self):
      count = 0
      for data in self.queue:
        if data:
          count += 1
      return count
```
