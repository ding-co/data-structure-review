# Stack

## _Outline_

> ADT

> Parentheses matching

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

## `Parentheses matching`

- 괄호 맞추기 문제 <br/>

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

## `Expression evaluation`

```python
# Infix; operator middle
# ex) (5 - 6) * 7 - 4 * 2
# Prefix; operator front
# ex) - * - 5 6 7 * 4 2
# Postfix; operator behind
# ex) 5 6 - 7 * 4 2 * -

# prefix and postfix don't need parentheses
# just only consider operand and operator orders
# --------------------------------------------------
# Infix -> Postfix
# Tip: Never change operand order!
#      just only change the operator order!

# ex1) A * B + C * D
# => A B * C D * +

# ex2) A * ((C / D) - (E / F)) - A * C
# => A C D / E F / - * A C * -

# ex3) a / b - c + d * e - a * c
# => a b / c - d e * + a c * -

# ex4) (a / (b - c + d)) * (e - a) * c
# => a b c - d + / e a - * c *

# How to code this algorithm?
# => Use Stack!! (LIFO)
# operands => just output (print)
# push operators to the stack
# ex) A + B * C => ABC*+
#     A * B + C => AB*C+
# when it meet operators, push
# but priority * > + => pop * and push next operator
# priority: *, / >> +, -
# priority equal or low => it can pop
# But, consider parentheses => ?
# --------------------------------------------------
# Postfix Evaluation
# operators; not change order
# last 2 operands => evaluate

# ex1) 4 5 6 * +
# => 4 30 +
# => 34

# ex2) 8 2 / 3 2 * +
# => 4 6 +
# => 10

# ex3) 17 10 + 3 * 9 /
# => 27 3 * 9 /
# => 81 9 /
# => 9

# ex4) 2 3 1 * + 9 -
# => 2 3 + 9 -
# => 5 9 -
# => -4

# Use Stack!!
# push operands to the stack
# and if meet operator, last pop() evaluate first pop()
# and then, push to stack again
# pop value is one (result) => the end

# how to code?
# ex) pseudocode
# list = ['a', 'b', '+', 'c', '-']
# for token in list:
#   if token is operand:      # if operand == '+': result = b + a
#     stack.push(token)       # elif oeprand == '-': result = b - a
#   else:
#     a = stack.pop()         # if pop() is None => error handling
#     b = stack.pop()
#     result = b operator a
#     stack.push(result)
# return stack.pop()
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
- Naming variable is very important!
- operand
- operator; + - \* /
- Stack algorithm; when push and pop?
- expression partition => token
- coding -> debugging repetition (skill up way)
- not typing the code, just see the book and understand!

#

## [Reference]

[Stack.py](https://github.com/ding-co/data-structure/blob/main/stack/stack.py)
