# Leetcode challenge in python
learn basic data structure and practice in python

## data structure 
* [Queue](https://docs.python.org/3/library/queue.html)
* Stack
* List
* Dict(Map)
* Tree

## Algorithm highlight
### Binary Tree DFS
```python
def preorder(root):
    if root:
        return [root.val] + preorder(root.left) + preorder(root.right)
    else:
        return []
```

## Environment Setup
### python installation
```zsh
    brew install pipenv
```
