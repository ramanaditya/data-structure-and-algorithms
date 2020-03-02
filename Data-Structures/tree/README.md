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

### 1. Preorder Traversal
### a). Recursive
```python
res = []
def inorderTraversal(root):
    # Base Case
    if not root:
        return
    # Recursive Case
    else:
        res.append(root.val)
        inorderTraversal(root.left)
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

### 2. Inorder Traversal
### a). Recursive
```python
res = []
def inorderTraversal(root):
    # Base Case
    if not root:
        return
    # Recursive Case
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

### 3. Postorder Traversal
### a). Recursive
```python
res = []
def postorderTraversal(root):
    # Base Case
    if not root:
        return
    # Recursive Case
    else:
        postorderTraversal(root.left)
        postorderTraversal(root.right)
        res.append(root.val)
    return res

# Time : O(n)

```

### b). Iterative
```python
def postorderTraversal(root):
    from collections import deque 
    stack = []
    res = deque()
    while root or len(stack) > 0:
        if root:
            stack.append(root)
            res.appendleft(root.val)
            root = root.right
        else:
            node = stack.pop()
            root = node.left
    return res

# Time : O(n)

```

