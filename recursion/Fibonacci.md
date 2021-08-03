# Recursion 3. <u>Fibonacci</u>

## _Consider_

> Time Complexity <br/>
> Iterative way vs Recursive way

<br/>

## `Fibonacci Sequence`

- F(n) = F(n-1) + F(n-2), F(0) = 0, F(1) = 1

```python
# Fibonacci - iterative way
# Time Complexity: O(n)
# Space Complexity: O(1)
def fibonacci_iterative(n):
  a, b = 0, 1
  # 0, 1, 1, 2, 3, 5, ... (n times)
  for _ in range(n):
    a, b = b, a + b
  return a

# n   a b
# 0   0 1
# 1   1 1
# 2   1 2
# 3   2 3
# 4   3 5
# ...

# ------------------------------------------------------------

# Fibonacci - recursive way 1 (naive)
# Time Complexity: O(2^n)
def fibonacci_recursive1(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  return fibonacci_recursive1(n-1) + fibonacci_recursive1(n-2)

# Fibonacci - recursive way 2 [more efficient]
# Hint: Memoization (caching) // subproblem repetition => caching
# Dynamic Programming (based on Recursive)
# Problem => Sub-problem + Memoize (Divide-and-Conquer)
# Recursive + memoization

# Time Complexity: O(n)
# Space Complexity: O(n)
def fibonacci_recursive2(n):
  global cache
  if cache[n]:
    return cache[n]
  if n == 0:
    result = 0
  elif n == 1:
    result = 1
  else:
    result = fibonacci_recursive2(n-1) + fibonacci_recursive2(n-2)
  cache[n] = result
  return result

cache = [None for _ in range(1000)]

# ------------------------------------------------------------

# Simple test cases
for i in range(50):
  print(f'iterative:  {i} = \t{fibonacci_iterative(i)}')
  print(f'recursive1: {i} = \t{fibonacci_recursive1(i)}')
  print(f'recursive2: {i} = \t{fibonacci_recursive2(i)}')
  print("-" * 30)
```

```python
# Python library - functools
import functools

# Decorator
# return value caching
@functools.lru_cache(maxsize=1000)
def fibonacci_recursive1(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci_recursive1(n-1) + fibonacci_recursive1(n-2)

# Simple test cases
for i in range(100):
  print(f'recursive1: {i} = \t{fibonacci_recursive1(i)}')
```

- Use python generator

#

## [Note]

- recursive; function calls times => catches the memory (as much depth)
