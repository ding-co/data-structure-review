# Stack

## _Outline_

> ADT

> Parenthesis matching

> Expression evaluation

<br/>

## `Stack`

- something piled
- function - push, pop (like a module)
- LIFO (Last In First Out) / FILO
- is_empty, peek

```python
# Stack Implementation
# Modularity (class)
class Stack:
  def __init__(self):
    self.items = []

  # Time Complexity: O(1)
  def push(self, item):
    self.items.append(item)

  # Time Complexity: O(1)
  def pop(self):
    if self.items:
      return self.items.pop()

  def is_empty(self):
    return not self.items

  def peek(self):
    if self.items:
      return self.items[-1]

# Simple test case
s = Stack()
print(s.is_empty())   # True
s.push("A")
s.push("B")
print(s.is_empty())   # False
s.push("C")
print(s.pop())        # C
print(s.peek())       # B
print(s.pop())        # B
print(s.pop())        # A
print(s.is_empty())   # True


# 1 item stack push or pop => time complexity: O(1)
# n items stack push -> time complexity: O(n)
#                    -> space complexity: O(n)

# LIFO => use stack???
```

#

## [Note]

- Memorizing good code is ok, but pre-understanding is necessary! <br/>
  Not just follow the code.
- Think as much as you can! + understand!
- Self-study -> see the book/internet, but not follow <br/>
  -> self-code again [repetition]
- ADT (Abstract Data Type) - Data + Behavior (like a black box)
- call stack
- Python; OOP (Object-Oriented Programming language) <br/>
  => use class (modularity)
- Ctrl + Shift + P => python select interpreter <br/>
  (can see VS Code setting - python version)
