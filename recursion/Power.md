# Recursion 2. <u>Power</u>

## _Consider_

> Time Complexity <br/>
> Iterative way vs Recursive way

<br/>

## `Power`

- x^n
- double power(double x, int n)

  ```python
  import timeit # check time
  import sys

  # increase recursion depth limit
  sys.setrecursionlimit(1500)

  # Power - iterative way
  # x^n = x * x ... x * x (n times)
  # ex) x^10 = x^9 * x = x^8 * x * x = ... = x * x ... * x (10 times)
  # Time Complexity: O(n)
  def power_iterative(x, n):
    result = 1
    for _ in range(n):
      result *= x
    return result

  # Power - recursive way 1
  # power(x, n) = power(x, n - 1) * x
  # Time Complexity: O(n)
  def power_recursive1(x, n):
    if n == 0:
      return 1
    return x * power_recursive1(x, n - 1)

  # Power - recursive way 2 (more effective)
  # hint: x^2n = (x^n)^2
  # x^n has three cases (n = 2m or 2m + 1 or 0)

  # case 1. x^2m (2m is an even number)
  #         => (x^m)^2

  # case 2. x^(2m+1) (2m+1 is an odd number)
  #         => (x^m)^2 * x

  # case 3. x^0 = 1

  # ex 1) x^10 = x^5 * x^5 = (x^2 * x^2 * x) * (x^2 * x^2 * x)
  #            = ((x * x) * (x * x) * x) * ((x * x) * (x * x) * x)
  #            10 -> 5 -> 2 -> 1 (4 times)
  # ex 2) x^1024; 1024 -> 512 -> ... -> 1 (11 times)

  # Time Complexity: O(ln n)
  # log2n (base:2, argument: n) = ln n / ln 2 => ln n
  def power_recursive2(x, n):
    if n == 0:
      return 1
    elif n % 2 == 0:
      return power_recursive(x, n / 2) ** 2
    else:
      return power_recursive(x, n - 1) * x

  # Simple test cases and compare performance time
  for i in range(11):
    print(f'2^{i}=\t{power_iterative(2, i)}\t{power_recursive1(2, i)} \
    \t{power_recursive2(2, i)}')

  # iterative way is more fast than recursive way 1
  # but increase ratio is similar (Time Complexity)
  print()
  print("iterative time: 2^1000", timeit.timeit('power_iterative(2, 1000)', \
  'from __main__ import power_iterative', number = 1000))
  print("recursive 1 time: 2^1000: ", timeit.timeit('power_recursive1(2, 1000)', 'from __main__ import power_recursive1', number = 1000))

  # however, recursive way 2 is the most fast way
  print("recursive 2 time: 2^1000: ", timeit.timeit('power_recursive2(2, 1000)', 'from __main__ import power_recursive2', number = 1000))
  ```

#

## [Note]

- In python, not use variable => use \_ (under bar/score)
- iterative way vs recursive way <br/>
  Most iterative ways are more fast (performance time) <br/>
  (cf. when recursive calls, in computer, remember where to jump and context switch <br/>
  so, it has additional jobs to do when function jump and return)
