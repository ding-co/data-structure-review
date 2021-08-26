## [Heap]

### _Concept_

- Complete Binary Tree (balanced)
- max heap: parent > children
- min heap: parent < children

- max heap

  |  T.C  | insert  | delete  |
  | :---: | :-----: | :-----: |
  | best  |  O(1)   |  O(1)   |
  | worst | O(ln n) | O(ln n) |

|          |             |  Push   |   Pop   |
| :------: | :---------: | :-----: | :-----: |
|  sorted  |    Array    |  O(n)   |  O(1)   |
|  sorted  | Linked List |  O(n)   |  O(1)   |
| unsorted |    Array    |  O(1)   |  O(n)   |
| unsorted | Linked List |  O(1)   |  O(n)   |
|          |    Heap     | O(ln n) | O(ln n) |

### _implementation_

- Tree
  - Link, Node (Linked List) => may be free to insert/delete <br/>
    but space increase (time performance is getting worse)
  - Array => only good for one direction (but tree is not)
  - use recursive way
- Heap

  - Array is very good (b/c all of node's position is fixed on linear data structure)
  - maximum number is limited but insert/delete is more fast than Linked List
  - not use recursive

- Heap with Array
  - Array, var(cnt)
  - index 0: root (index n)
  - parent(n) => Math.floor((n-1)/2)
  - leftChild(n) => (2 \* n + 1)
  - rightChild(n) => (2 \* n + 2)

#

## [Note]

- Complete binary tree <br/>
  if, we know the number of nodes <br/>
  we can know the tree's shape
- max heap; max is a captain <br/>
  check parent always bigger than subtree
- max/min heap => priority queue
- Heap is not a fully sorted <br/>
  just part of sort that we want
- recursive call => use stack memory
- python: heapq library
