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

## [Reference]

[Stack.py](https://github.com/ding-co/data-structure/blob/main/stack/stack.py)
