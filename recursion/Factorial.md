# Recursion 1. <u>Factorial</u>

## _Consider_

> Time Complexity <br/>
> Iterative way vs Recursive way

<br/>

## `Factorial`

- n! = n \* (n-1)! [Recursion]
- 0! = 1

```python
# Recursive way
def factorial_recursive(n):

  # Basic Sol 1.
  # [Use Mathematic definition]
  if n > 0:
    return n * factorial_recursive(n - 1)
  return 1

  # Reference Sol 2.
  # [Use one line if-else statement (Python style)]
  # return n * factorial_recursive(n - 1) if n > 0 else 1

  # Reference Sol 3.
  # [Use Short-circuit evaluation]
  # return (n > 0 and n * factorial_recursive(n - 1)) or 1

# factorial_recursive(3)
# => 2 + factorial_recursive(2)
# => 2 + 2 + factorial_recursive(1)
# => 2 + 2 + 2 + factorial_recursive(0)
# => 2 + 2 + 2 + 2
# => 8

# How many factorial_recursive function calls?
# factorial_recursive(n) => (n + 1) times
# So, Time Complexity: O(n)

# -----------------------------------------------------------------

# Iterative way
def factorial_iterative(n):

  # multiplication identity: 1 (not affect to result)
  result = 1                # 1 (performance times)

  # range; start: inclusive, stop: exclusive
  for i in range(1, n + 1): # n
    result *= i             # n
  return result             # 1

# Cost function: f(n) = 2n + 2
# => Time Complexity: O(n) is meaningful!

# -----------------------------------------------------------------

# Simple Test Cases
for i in range(10):
  print(f'Recursive: {i}! = {factorial_recursive(i)}')
  print(f'Iterative: {i}! = {factorial_iterative(i)}')
  print("-" * 25)
```

```python
# Compare Test time
# Recursive way vs Iterative way

# timeit module
# default: count 100,000 times each case => check time
# unit: sec
import timeit

# Recursive way
def factorial_recursive(n):
  if n > 0:
    return n * factorial_recursive(n - 1)
  return 1

# Iterative way
def factorial_iterative(n):
  result = 1
  for i in range(1, n + 1):
    result *= i
  return result

# Increase ratio is similar
for i in range(20):
  recursive_time = timeit.timeit(f'factorial_recursive({i})', \
  'from __main__ import factorial_recursive', number = 10)

  iterative_time = timeit.timeit(f'factorial_iterative({i})', \
  'from __main__ import factorial_iterative', number = 10)

  print(f'Recursive: {i}! = {factorial_recursive(i)}', \
  Time: {recursive_time})

  print(f'Iterative: {i}! = {factorial_iterative(i)}', \
  Time: {iterative_time})

  print("-" * 80)
```

#

## [Note]

- Recursive; useful for Tree <br/>
  Recursive: call myself cf) Math - recurrence relation, induction <br/>
  Use myself -> represent before step ex) n -> (n - 1) call <br/>
  And **always consider the end condition** (to prevent infinite loop) <br/>
  Complex problem -> simple problem
- Iterative way; Use for/while loop statement
- VS Code; screencast mode; can see short-cut key real-time
- RecursionError: maximum recursive depth default: 996 times (python) <br/>
- Short-Circuit evaluation <br/>
  True or False => front is True, so need not to see the behind => So, result is True <br/>
  True and True => front is True, so we have to see the behind => behind is True => So, result is True
- e(E) = 10
