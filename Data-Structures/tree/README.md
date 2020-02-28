# Tree

## Node
```python
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

```

## Traversal

### 1. Inorder Traversal
### a). Recursive
```python
res = []
def inorderTraversal(root):
    if not root:
        return
    else:
        inorderTraversal(root.left)
        res.append(root.val)
        inorderTraversal(root.right)
    return res

# Time : O(n)

```

### b). Iterative
```python
def inorderTraversal(root):
    stack = []
    res = []
    while root is not None or len(stack) > 0:
        while root is not None:
            stack.append(root)
            root = root.left
        root = stack.pop()
        res.append(root.val)
        root = root.right
    return res

# Time : O(n)

```