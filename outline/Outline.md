# Outline

## _Prerequisite_: Python programming (select one of programming Languages)

<br/>

- Coding test: Data Structure & Algorithm
- Data Structure is a basis version of an Algorithm.
- Data Structure: way of organizing data in a computer <br/>
  (ex. array, graph, set, tree, ...)
- Algorithm: Learning how to solve the problem <br/>
  Problem Solving Order; step-by-step set of operations
- Developing our thinking power about the same problem.
- How to solve the problem efficiently?
- Looking for good code! => very famous problem and solution
- Don't memorize the code! Always think constantly!!!
- after that see the famous solution and then, realize
- Think what is the advantage and disadvantage of this algorithm way?

<br/>

## **Question: How to hand out the name tags to event participants efficiently??** <br/>
### (ex. 1000 name tages)

<br/>

### _[In computer view, find name tag for one person]_

<br/>

### possible #1. <u>Sequential(Linear) search</u>: check one by one

- Worst Case: O(n)
- Best Case: O(1)

<br>

### possible #2. <u>Type of Hash</u>: grouping by Last name (ex. Korean name 14 group)

- Worst Case: O(n) ex) Last name only 'Kim' 1000 people
- Best Case: O(1)

<br/>

### possible #3. <u>Binary search</u>: **_already sorted_**, check middle tag and compare to person's name <br/>
### and then narrow the range (repeat until find)

- Worst Case: O(logn)
- Best Case: O(1) <-- Best case is not meaningful. it's just for lucky.

<br>

### possible #4. <u>Parallelization</u>: 10 tags each for 100 people

- Worst Case: O(n / numbers of people)

<br/>

## Abstraction: Complex problem -> simple black box (hide complex thing)

## We don't know detail inner principles, we hide complex things covered with black box, <br/>
## and then just use user interfaces. (repeat and make bigger block)

<br/>

## ADT (Abstract Data Type)

- Data
- Behavior

> make it to a black box
>
> - encapsulation
> - change localization
> - flexibility

<br/>

## **What is a standard of Good Algorithm?**

> Correctness (not depend on luck)

> Efficiency
>
> - **Time** (consider worst case)
> - **Space**
> - Battery consumption
> - Heat, ...

## Time Complexity

- Best case
- Average case
- `Worst case`

<br/>
