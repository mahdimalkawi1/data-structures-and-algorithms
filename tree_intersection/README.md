# Find common values in 2 binary trees.


Write a function called tree_intersection that takes two binary trees as parameters.

## Whiteboard Process

![ white board](./assets/Untitled%20(31).jpg)

## Approach & Efficiency

- Time Complexity:
The time complexity of the code is O(n). 
- Space Complexity:
The space complexity of the code is also O(n).
## Solution

``` python 
def tree_intersection(tree1,tree2):
   
    hash_table = HashTable()
    nodes = tree1.post_order()
    intersection = []
    for node in nodes:
      hash_table.set(node,node)

    nodes = tree2.post_order()
    for node in nodes:
      if hash_table.has(node):
         intersection.append(node)
    return intersection

```

### [Tests](./tests/test_tree_intersection.py)


