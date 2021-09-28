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

  - Rudolf Bayer (1972)
  - / Used in Linux Kernel, C++ STL, Java
  - Binary Search Tree based
  - Properties
    - Root is Black
    - All leaves (NULL) are Black (new node is Red)
    - All path's Black node numbers are same (Black-Height)
  - Insertion
    1. Root? -> Black, the end
    2. Parent == Black? -> OK, the end
    3. Parent == Red, Parent's friend (uncle) == Red <br/>
       => Recolor & Recheck (Goto 1); <br/>
       Parent and Uncle, both make it to all Black (two nodes) <br/>
       and parent, uncle's parent node make it to Red (one node)
    4. Rotate & Recolor
       - LL
         - right rotate & recolor
       - RR
         - left rotate & recolor
       - LR
         - left rotate (make it to LL)
         - right rotate
         - recolor
       - RL
         - right rotate (make it to RR)
         - left rotate
         - recolor
  - T.C: insert/update/delete O(log n)

- B-Tree
  - Rudolf Bayer, Edward M. McCreight (1971)
  - Property
    - Every node has at most m children
      - ex) 3 children => maximum degree 3 => max key 2
    - Every non-leaf node (except root) has at least [m/2] children
    - The root has at least two children if it is not a leaf node
    - A non-leaf node with k children contains k-1 keys
    - All leaves appear in the same level
  - 2-3 Tree: B-Tree of order 3
  - Variants(improvement): B+ Tree, B\* Tree

#

## [Note]

- Practice

  - [Reference 1](https://people.ok.ubc.ca/ylucet/DS/Algorithms.html)
  - [Reference 2](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html)

- AVL Tree
  - left subtree, right subtree height difference 1
  - rebalancing too much
- Red-Black Tree
  - prevent red - red
  - one subtree height => h, other subtree height maximum 2\*h
- B-Tree
  - not rotate
  - split => 100% balanced
  - all nodes' heights are same
  - pre-selected node's maximum values
  - utilization
    - Database (file structure)
    - index => B+ Tree
    - B+ Tree
      - non-leaf node => duplicated key
      - leaf node => sorted
