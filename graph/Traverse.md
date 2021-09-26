## [Graph]

### _Traverse_

- Traverse (visit all nodes once, let connected graph)

  - set flag (check visited) for preventing infinite circulation
  - DFS; Depth-First-Search
    - use Stack (LIFO)
  - BFS; Breadth-First-Search
    - use Queue (FIFO)
    - level first search
  - while !s(q) empty: <br/>
    n <- s(q).pop (q일때는 popleft) <br/>
    operations for each visit ex) print node <br/>
    n.visited = True(1) <br/>
    s(q).push(connected + not visited nodes)

#

## [Note]

-
