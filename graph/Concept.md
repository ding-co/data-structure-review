## [Graph]

### _Concept_

- Graph => Vertex(Node), Edge(Link)
- tree is a type of Graph

- Outline
  - Graph Concept / Notations
    - Graph
      - G = (Vertex, Edge)
      - Vertex(Node), Edge(Link) => set { }
      - empty graph also can be a graph
      - no edge, only vertex also can be a graph
    - Notations
      - Undirected / Directed Graph
        - directed graph; edge's start and begin are important
      - Weighted Graph
        - we can put extra data to vertex or edge (weight)
      - Network? Node? Link?
        - Graph(Network) => Vertex(Node), Edge(Link)
        - ex) social network
          - following (me -> friend), follower (friend -> me)
          - User (Vertex), Relationship (Edge), directed
      - Adjacent: Vertex - Vertex (connected)
      - Incident: Edge - Vertex (Edge is out of a Vertex)
      - Degree / In-degree / Out-degree
        - degree; how many edges connected to a vertex
        - directed graph
          - In-degree; edge into the vertex
          - Out-degree; edge out of the vertex
      - Path / Simple path
        - path; vertex -> vertex (way)
        - simple path; not equal to shortest path, not cyclic (not pass by the same vertex)
      - Cycle
        - one vertex -> return to self
      - DAG (Directed Acyclic Graph): Direct + Acyclic
        - ex) pre-requisite course
      - Connected / Disconnected / Complete Graph
        - completed graph; all vertex's edge fully-connected
- Representations (use computer)
- Algorithms
  - Traverse: DFS, BFS
  - Minimum Spanning Tree: Kruskal, Prim
  - Shortest Path: Dijkstra, Floyd
  - Topological Sort: Kahn, DFS

#

## [Note]

- Tree Representation
  - BST; use links
  - Heap; use array (let only BT)
- Graph; just focus on vertex and edge connection state! <br/>
  (not meaningful about exact coordinates/position)
- topological (what and what are connected)
- Tree => acyclic (cycle X) + fully-connected + Graph
  - acyclic <br/>
    ex 1) course pre-requisite; python -> data structure -> DB -> Project <br/>
  - fully-connected
    - try (X) <- not fully-connected (disconnected)
- if in-degree so many => influencer (social network analysis)
- cyclic <-> acyclic
- sub-graph
  - subset of a graph
  - empty also can be a subset
- graph utilization
  - ex 1) social network analysis
  - ex 2) website search engine (website links)
    - sorting and represent to clients
    - google (pageRank, graph analysis -> ranking)
  - ex 3) Bio Informatics (Bio + Computer Science)
