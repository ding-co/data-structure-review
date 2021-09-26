## [Graph]

### _Shortest Path_

- Shortest Path: Dijkstra, Floyd
- Dijkstra algorithm
  - choose one start point
  - each edge has a weight (distance, value)
  - find the minimum cost path
  - representation; adjacency matrix
    - if can't go => set value to Infinity
  - use two arrays and one queue
    - distance
    - from (source)
    - queue
  - while !q empty? (minHeap) <br/>
    v <- q.dist pop
  - T.C: O(|V|^2), if use minHeap => O(|V|log |V|)
- Floyd (Floyd-Warshall) algorithm
  - Find all shortest paths
  - for all vertices -> Dijkstra (OK..)
  - use three nested for loop (element in all vertices) <br/>
    and then, compare direct way to via way => if via way is more efficient => update
  - T.C: O(|V|^3)

#

## [Note]

- Shortest Path utilization
  - computer network delay latency
- A\* Algorithm; find the path algorithm
  - reduce useless cases
  - Seoul - Pusan path
  - navigation
  - game; waypoint
- Dijkstra Algorithm; find the all possible path
