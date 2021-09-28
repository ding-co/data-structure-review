## [Search]

### _Balanced Search Tree_

- AVL Tree

  - Georgy Adelson-Velsky and Evgenii Landis (1962)
  - BF (Balance Factor): Height(L) - Height(R) -> {-1, 0, 1}
  - only allow balance difference 1
  - Binary Search Tree based
  - each node has a balance factor
    - left subtree height - right subtree height (difference)
  - if difference >= 2 => adjust!
    1. LL
       - right rotate
    2. RR
       - left rotate
    3. LR
       - rebalancing
         - left rotate (make to LL)
         - right rotate
    4. RL
       - rebalancing
         - right rotate (make to RR)
         - left rotate
  - T.C (Worst Case)
    - insert: O(log n) + Rebalancing (O(log n)) => O(log n)
    - delete: O(log n)
    - search: O(log n)

- Red-Black Tree

- B-Tree

#

## [Note]

- Practice
  - [Reference 1](https://people.ok.ubc.ca/ylucet/DS/Algorithms.html)
  - [Reference 2](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html)
