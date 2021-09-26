## [Graph]

### _Minimum Spanning Tree_

- Minimum Spanning Tree: Kruskal, Prim
  - Minimum Spanning Tree
    - Spanning Tree: A subgraph that is a tree including all vertices
    - Minimum (cost / weight) Spanning Tree
      - Greedy Algorithm (Naive)
        - Kruskal's algorithm
          - repeat until include all vertices <br/>
            (tree; acyclic + fully-connected => vertex n , edge => n - 1) <br/>
            => while result == n-1
          - e = pick the smallest edge (weight)
          - e cycle? <br/>
            yes: x <br/>
            no: result <- e
          - T.C => pre-sort: O(|E|log |E|), loop: O(|E|) <br/>
            cycle test? -> bfs, dfs (naive, O(|V|)) <br/>
            cycle test => Union-find / Merge-find algorithm! <br/>
            (Disjoin-set data structure => O(1), amortized) <br/>
            so, T.C => O(|E|log |E|) // sorting
          - S.C => O(|E|) ? (weight)
        - Prim's algorithm
          - start at any vertex
          - result <- {V}
          - while |V|
          - pick the smallest vertex (check connected edge weight)
          - grouping, pick the smallest vertex, repeat until pick all vertices
          -

#

## [Note]

- MST
  - Just focus on total cost and connection
  - not focus on shortest path
  - ex) distribution transportation optimization <br/>
    network communication optimization (install cost)
- Minimum: minimize cost / weight
- Spanning: stretch and cover all vertices
- Tree: acyclic + fully-connected graph
- Greedy (ignorant)
- MST algorithm
  - Kruskal; pick edges in a greedy way, cycle test
  - Prim; pick vertices in a greedy way
    - how to get minimum cost edge?
      - put all vertices to an array
      - initiate all value to Infinity
      - find a way with every group and update repeat
  - cycle test?
    - use FIND-SET algorithm
      - check the same group vertices
      - combine with other group (ok)
      - if combine with same group => cycle
      - ex) catch tail game
      - array
        - remember each item's boss
        - let, priority: alphabet order to before
        - compare to each group's boss
          - if same boss => cycle
        - T.C: O(|V|)
          - => make trick
            - update all vertices' boss to the highest boss (height 1 tree)
            - T.C: O(1); amortized (asymptotic)
