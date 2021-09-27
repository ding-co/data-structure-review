## [Graph]

### _Topological Sort_

- For DAG (Directed Acyclic Graph)
  - ex) pre-requisite course <br/>
    project dependency <br/>
    work sequence <br/>
    module/compile dependencies
  - sort focus on connection state
- Applications?
- Algorithm
  - Kahn's algorithm
    - find in-degree 0 vertex
    - exclude edge connected vertex which is pre-selected
    - check and repeat
  - Depth-first-search
    - select any vertex
    - and go until find the last vertex
    - print reverse order

#

## [Note]

- DFS
  - use stack
  - recursive
