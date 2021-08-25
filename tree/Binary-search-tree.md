## [Binary Search Tree]

### _name tag problem_

- already sorted name tags
- binary search => O(log n)
- how to insert/delete extra name tags??
  - we can use linked list <br/>
    but search is slow => O(n)
  - use binary tree?

### _Binary Search Tree_

- Binary Tree
  - definition: { } or {LBT, self, RBT}
- Binary Search Tree
  - definition: { } or {LBST, self, RBST} + Condition(LBST < self < RBST)
  - recursive
    - all of my Left sub tree values are smaller than me
    - all of my right sub tree values are greater than me
  - Time Complexity => O(log n) for search one key

### _ADT_

- insert

  - let, all keys are different (if same key => not insert) <br/>
    (ex. student id)

  ```python
  # insert 10
  # insert 5
  # insert 13
  # insert 4
  # insert 9
  # insert 8
  # insert 11
  # insert 2

  # root(empty pointer) -> Node(empty, 10, empty)
  #                  10
  #               5     13
  #             4   9  11
  #            2   8

  # tree height: 4
  # search 10: root read, the end (read only one time)
  # search 8: 10 -> 5 -> 9 -> 8 (read 4 times)
  # search 7: 10 -> 5 -> 9 -> 8 -> empty (read 4 times)
  ```

  |   T.C    |  Insert  |  Search  |
  | :------: | :------: | :------: |
  |   Best   |   O(1)   |   O(1)   |
  |  Worst   |   O(n)   |   O(n)   |
  | Balanced | O(log n) | O(log n) |

- delete
- search

### _Threaded Binary Tree_

- not BST
- Threaded BT
- if a node's left, right => None <br/>
  ex. inorder traverse; point inorder before/ inorder after node...
- set flag => thread, link
- we can do inorder traverse without recursive
- Threaded; use empty pointer(link)

### _etc_

- Winner Tree
- Loser Tree
- Forest
  - Try: not connected tree
  - Try group => forest

#

## [Note]

- key (for search); string, number,... <br/>
  if we can find key, we can search with key!
- empty binary search tree (leaf node)
- if we can code with hands, we have to code with computer too <br/>
  next, analyze performance (time/space complexity)
- Focus on worst case
- sorted data => insert to binary search tree (skewed/unbalanced) <br/>
  (similar to linked list...)
- BST; balanced => height: log n, T.C: O(log n) <br/>
  worst(skewed) => height: n, T.C: O(n), similar to linked list
- we will learn how to convert skewed tree into balanced tree <br/>
  => if we want to insert/search data quickly, we will use balanced tree!
