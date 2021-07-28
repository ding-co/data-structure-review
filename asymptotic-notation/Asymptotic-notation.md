# Asymptotic Notation

> Algorithm performance time is related to input size <br/>
> Time Complexity; consider very big input size N <br/>
> So, not meaningful for coefficient or constant <br/>
> It's just depend on N (input size)

<br/>

## _Big O_

<img src="https://www.freecodecamp.org/news/content/images/2021/06/0_cyqWw3UxODl-wqJi.jpg" width="500" height="350"> <br/>
[Reference](https://www.freecodecamp.org/news/big-o-notation-why-it-matters-and-why-it-doesnt-1674cfa8a23c/)

- Let, O(g(x)) means always f(x) <= K \* g(x)
- There are too many options for Big O
- So, select the smallest range of Big O (meaningful) <br/>
  (cf. if log function; just ignore base => use base e <br/>
  so use log or ln)
- Performance time standard: O(logn) >> O(n); O(logn) is more scalable(extensible)
- Worst case

<br/>

## _Big Omega_

- f(x) >= k \* g(n)
- At the earliest, f is slower than g.
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
[Reference](https://www.geeksforgeeks.org/analysis-algorithms-big-o-analysis/)

- O(1): constant (complexity)
- O(logn): logarithmic
- O(n): linear
- O(n^2): quadratic <br/>
  (cf. O(n^k) for k >= 1: Polynomial)
- O(n^3): cubic
- O(2^n), O(k^n), O(n!): exponential

<br/>

### Quiz 1) logn ?(log8n) <= 8 is base, n is argument

- ? => Big O? Big Omega? Big Theta?
