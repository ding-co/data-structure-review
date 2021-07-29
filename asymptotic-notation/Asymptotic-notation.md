# Asymptotic Notation

> Algorithm performance time is related to input size <br/>
> Time Complexity; consider very big input size N <br/>
> So, not meaningful for coefficient or constant <br/>
> It's just depend on N (input size)

<br/>

## _Big O_

<img src="https://www.freecodecamp.org/news/content/images/2021/06/0_cyqWw3UxODl-wqJi.jpg" width="500" height="350"> <br/>

- O(g(x)) means always f(x) <= K \* g(x)
- There are too many options for Big O
- So, select the smallest range of Big O (meaningful) <br/>
  (cf. if log function; just ignore base => use base e (Euler's constant) <br/>
  so, use log or ln)
- Performance time standard: O(logn) >> O(n); O(logn) is more scalable(extensible)
- Worst case

<br/>

## _Big Omega_

- f(x) >= k \* g(n)
- At the earliest f, f is slower than g.
- Best case

<br/>

## _Big Theta_

- It can be Big Omega and Big O
- Both bounding
- Average case

<br/>

## Worst case analysis => use Big O notation <br/>

(Algorithm evaluation standard)

<br/>

## Big O comparison

<img src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/mypic.png" width="500" height="250"> <br/>

- O(1): constant (time complexity)
- O(logn): logarithmic
- O(n): linear
- O(n^2): quadratic <br/>
  (cf. O(n^k) for k >= 1: Polynomial)
- O(n^3): cubic
- O(2^n), O(k^n), O(n!): exponential

<br/>

### Example. logn ?(log8 n) <- 8 is a base, n is an argument

- ? => Big O? Big Omega? Big Theta?

- The answer is Big O

<br/>

## How to prove the Big O notation?

- Big O's definition: abs(f(x)) <= C \* abs(g(x)) for all x >= k (C, k > 0, constant)

<br/>

> ### Example 1. f(n) = 4n^2 + 2n - 1, Prove: O(n^2)

```
Prove: abs(4n^2 + 2n - 1) <= C * abs(n^2), for all n >= k

let, k = 1, C = 6

=> abs(4n^2 + 2n - 1) <= 6 * abs(n^2), for all n >= 1

=> 4n^2 + 2n - 1 <= 6 * n^2, for all n >= 1
(because 4n^2 + 2n - 1 and n^2 are increase function when n >= 1)

<Use Inequality method>

=> 4n^2 + 2n - 1 < 4n^2 + 2n <= 4n^2 + 2n^2

=> 4n^2 + 2n - 1 < 4n^2 + 2n <= 6n^2

=> 4n^2 + 2n - 1 < 6n^2

so, f(n) = O(n^2)

* Tip) We just prove C, k (constant, greater than 0, real number) exist on that inequality

* Big Theta; prove Big O and Big Omega both cases
```

<br/>

> ### Example 2. f(n) = n + 30, Prove: O(n^3)

```
Prove: abs(n + 30) <= C * abs(n^3), for all n >= k, [C, k exists]

let, C = 31, k = 2

=> abs(n + 30) <= 31 * abs(n^3), for all n >= 2

=> n + 30 <= 31 * n^3, for all n >= 2
(because n + 30 and n^3 are positive number when n >= 2)

=> n + 30 <= 31 * n^3

<Use Division method>

=> ((n + 30) / (31 * n^3)) <= 1

=> (1 / (31 * n^2) + 30 / (31 * n^3)) <= 1

=> (1 / (31 * n^2) + 30 / (31 * n^3)) <= (1 / 31) * (1 / 2^2) + (30 / 31) * (1/ 2^3) <= 1
(because 1 / (31 * n^2) and 30 / (31 * n^3) are decrease function when n >= 2)

so, f(n) = O(n^3)


cf). <Use Inequality method>

    n + 30 <= 31 * n^3

=>  n + 30 < n^2 * (n + 30) < n^3 + 30 * n^2 * n (= 31 * n^3)

=>  n + 30 <= 31 * n^3
```

<br/>

> ### Example 3. f(n) = log2 n (base: 2, argument: x), Prove: O(n)

```
<Use Graph method>

let C = 100, k = 32

=> (left term) log2 32 = 5

   (right term) 100 * 32 = 3200

=> 5 <= 3200 (that difference is getting bigger as check two function graph)

So, f(n) = O(n)
```

#

## [Reference]

[Reference1](https://www.freecodecamp.org/news/big-o-notation-why-it-matters-and-why-it-doesnt-1674cfa8a23c/)
[Reference2](https://www.geeksforgeeks.org/analysis-algorithms-big-o-analysis/)
