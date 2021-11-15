# Recursion 4. <u>Hanoi</u>

## _Consider_

> Time Complexity

<br/>

## `Tower of Hanoi`

- void hanoi(int n, char from, char to, char tmp)
- A small disc should be above a large disc
- src - tmp - des <br/>
  (source, temporary, destination)

  ```python
  # hanoi - recursive way
  #    hanoi(n, src, des)
  # => hanoi(n-1, src, tmp)
  # => move(n, src, des)
  # => hanoi(n-1, tmp, des)

  # n   m(move)
  # 1   1
  # 2   3
  # 3   7
  # 4   15
  # 5   31
  # ...

  # Time Complexity: O(2^n)
  step = 0

  def move(disc, src, des):
    global step
    step += 1
    print(f'disc {disc}: move from [{src}] to [{des}]')

  def hanoi_recursive(n, src, des, tmp):
    if n > 0:
      hanoi_recursive(n-1, src, tmp, des)
      move(n, src, des)
      hanoi_recursive(n-1, tmp, des, src)

  # Simple test case
  print("3 Disc from A to B")
  print("=" * 30)
  hanoi_recursive(3, "A", "B", "C")
  print("=" * 30)
  print(f'{step} Steps')
  ```

#

## [Note]

- recursive: n problems -> (n-1) sub-problems <br/>
  f(n) = f(n-1) ... <br/>
  edge case (end condition)

#

## [Summary]

- factorial: iterative O(n), recursive O(n)
- power: iterative O(n), recursive O(ln n)
- fibonacci: iterative O(n), recursive O(n) - DP or O(2^n)
- hanoi: iterative too hard, recursive O(2^n)
