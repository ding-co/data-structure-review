## [Tree]

### _Theoretical concept_

- Graph: V = {}, E = {}
- empty, 1 node, 2 nodes connected,... => Tree OK.
  - empty (N, E both nothing => Tree OK)
- but if, circulating => Tree X
- if, only 2 nodes (not connected) => Tree X
- All Trees are type of Graph
- Tree: Fully-connected graph + Acyclic <br/>
  (shape is not an important, just only focus on connection relationship)
  - |V| = |E| + 1 (the number of Vertex/Edge)

### _Tree Utilization_

- Organization chart
- genealogy
- Hierarchical structure
  - Folder structure
- Recursive
  - subtree is part of tree

### _Terminology_

- Node / Edge
  - Node (data connected by edge)
  - Edge (connect line)
- Root: the parent node of everything (start point node)
- Parent / Child
  - close to Root => Parent Node
  - far from Root => Child Node
- Siblings
  - children from same parent node
- Ancestor / Descendant
- Terminal node / Non-terminal node
  - terminal node (leaf node)
  - Non-leaf node (internal node)
- Level
- Height / Depth
- Degree
  - how many children from a parent node
- Subtree
  - a part of tree
  - one node / nothing can be a subtree

### _Definition_

- Tree: Graph, Full-connected, Acyclic

### _Tree representation way_

- Linked List?
  - Link, Node => Possible! (one node for multiple links)
- Array?
  - Possible!

### _Binary Tree ADT_

- Objects: empty or (root + left binary tree + right binary tree)
- Functions
  - Create
  - isEmpty
  - MakeBT(LBT, item, RBT)
  - LChild
  - RChild
  - Data (into the Node)

### _Properties_

- Maximum number of nodes

  - level i
  - Maximum nodes => 2^i - 1 (the number of nodes)
  - minimum nodes => i

- Full Binary Tree

  - all level => Maximum nodes

- Complete Binary Tree

  - a tree that's full from the front (from left-side)
  - full binary tree can be a complete binary tree
  - if we know the number of nodes, we can know the tree's full shape!

### _Traverse_

- Inorder
  - Left - Self - Right
- Preorder
  - Self - Left - Right
- Postorder

  - Left - Right - Self

- Depth-First Search
- Breadth-First Search

```python
# binary tree example
#         A
#     B     C
#   D   E F   G
#      H   I

# root node: A

# Inorder traverse
# D - B - H - E - A - F - I - C - G

# Preorder traverse
# A - B - D - E - H - C - F - I - G

# Postorder traverse
# D - H - E - B - I - F - G - C - A

# DFS (Use Stack)
# A - B - D - E - H - C - F - I - G
# A - C - F - I - G - B - E - H - D (OK)

# BFS (Use Queue)
# Level First Search
# A - B - C - D - E - F - G - H - I
```

### _Recursive Operation_

- two trees equal?
- copy

#

## [Note]

- Discrete Mathematics
- Node (Vertex)
- Edge (Node - Node connect line)
- Tree is also a module (black box)
- Binary Tree: the number of children node is maximum 2 (0 ~ 2)
- Tree (generally recursive)
