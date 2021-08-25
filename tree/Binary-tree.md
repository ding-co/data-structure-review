## [Binary Tree]

```python
from collections import deque

class BinaryTree:
  class Node:
    def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None

  def __init__(self):
    self.root = None

  # _ starts mean inner function (private)
  def _preorder(self, node):
    if node:
      print(node.value, end=" > ")
      self._preorder(node.left)
      self._preorder(node.right)

  def _inorder(self, node):
    if node:
      self._inorder(node.left)
      print(node.value, end=" > ")
      self._inorder(node.right)

  def _postorder(self, node):
    if node:
      self._postorder(node.left)
      self._postorder(node.right)
      print(node.value, end=" > ")

  def traverse_preorder(self):
    print("Preorder: ", end="")
    self._preorder(self.root)
    print()

  def traverse_inorder(self):
    print("Inorder: ", end="")
    self._inorder(self.root)
    print()

  def traverse_postorder(self):
    print("Postorder: ", end="")
    self._postorder(self.root)
    print()

  def dfs(self):
    print("dfs: ", end="")
    stack = []
    stack.append(self.root)
    while stack:
      node = stack.pop()
      if node:
        print(node.value, end=" > ")
        stack.append(node.right)
        stack.append(node.left)
    print()

  def bfs(self):
    print("bfs: ", end="")
    queue = deque()
    queue.append(self.root)
    while queue:
      node = queue.popleft()
      if node:
        print(node.value, end=" > ")
        queue.append(node.left)
        queue.append(node.right)
    print()

  def _height(self, node):
    if not node:
      return 0
    left_height = self._height(node.left)
    right_height = self._height(node.right)
    return max(left_height, right_height) + 1

  def height(self):
    return self._height(self.root)

# Simple Test Case

#           A
#       B       C
#     D   E   F   G
#      H     I J

tree = BinaryTree()
tree.root = BinaryTree.Node("A")
node1 = BinaryTree.Node("B")
node2 = BinaryTree.Node("C")
node3 = BinaryTree.Node("D")
node4 = BinaryTree.Node("E")
node5 = BinaryTree.Node("F")
node6 = BinaryTree.Node("G")
node7 = BinaryTree.Node("H")
node8 = BinaryTree.Node("I")
node9 = BinaryTree.Node("J")

tree.root.left = node1
tree.root.right = node2
node1.left = node3
node1.right = node4
node2.left = node5
node2.right = node6
node3.right = node7
node5.left = node8
node5.right = node9

tree.traverse_preorder()
tree.traverse_inorder()
tree.traverse_postorder()

tree.dfs()
tree.bfs()

print(tree.height())
```

```python
# reference
class BinaryTree:
  class Node:
    def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None

    def traverse_inorder(self):
      if self.left:
        self.left.traverse_inorder()
      print(self.value, end=" > ")
      if self.right:
        self.right.traverse_inorder()

  def __init__(self):
    self.root = None

  def traverse_inorder(self):
    if self.root:
      self.root.traverse_inorder()
    print()
```

#

## [Note]

- Tree algorithm point => recursive
