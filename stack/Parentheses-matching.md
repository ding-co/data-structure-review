## `Parentheses matching`

```python
# ex) (a + b) - c       (OK)
#     ((a + b) - c) * 2 (OK)
#     (((a + b)) * 2    (NO)

# idea 1. count open/close parentheses numbers
#         open numbers == close numbers => True
#         but edge case: ) a + b ( => NO!

# idea 2. declare count variable
#         (initial value: 0, not negative, only meet 0)
#         if encounter open parentheses => count += 1
#         else => count -= 1
#         but edge case: [, ], {, } => how to handle this type?

# idea 3. declare three type of count variables
#         (initial value: 0, not negative, only meet 0)
#         if three type of variables => all 0 => True
#         but edge case: ({a)} => ????
# -------------------------------------------------------------------
# idea 4. use Stack concept!
#         if meet open parentheses, push
#         after if meet close parentheses, pop and compare
#         after if stack is empty => OK

# implementation (idea 4)
from stack import Stack

# Naive
def parentheses_test1(str):
  s = Stack()
  for ch in str:
    if ch == "(" or ch == "{" or ch == "[":
      s.push(ch)
    elif ch == ")" or ch == "}" or ch == "]":
      pair = s.pop()
      if pair and (\
        (pair == "(" and ch == ")") or \
        (pair == "{" and ch == "}") or \
        (pair == "[" and ch == "]") \
        ):
          continue
      else:
        return False

  return s.is_empty()

# Use dictionary
def parentheses_test2(str):
  s = Stack()
  LEFT_PARENTHESES = {"(": 1, "{": 2, "[": 3}
  RIGHT_PARENTHESES = {")": 1, "}": 2, "]": 3}
  for ch in str:
    left = LEFT_PARENTHESES.get(ch, 0)
    right = RIGHT_PARENTHESES.get(ch, 0)
    if left > 0:
      s.push(left)
    elif right > 0:
      pair = s.pop()
      if not pair or pair != right:
        return False

  return s.is_empty()

# Simple test cases
print(parentheses_test1("(a+b)"))  # True
print(parentheses_test1("((a+b)")) # False
print(parentheses_test1("(a+b))")) # False
print(parentheses_test1("({a+b}-({[C*D]}))")) # True
print(parentheses_test1("({a+b)}")) # False
```

#

## [Reference]

[Stack.py](https://github.com/ding-co/data-structure/blob/main/stack/stack.py)
