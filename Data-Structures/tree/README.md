# Tree

## Traversal

### Inorder Traversal
### 1. Recursive
```python
res = []
def inorder(root):
    if not root:
        return
    else:
        inorder(root.left)
        res.append(root.val)
        inorder(root.right)
    return res

```