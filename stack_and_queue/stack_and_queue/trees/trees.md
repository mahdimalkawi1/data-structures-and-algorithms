# Trees.


## Whiteboard Process



## Approach & Efficiency
### add:
- Time Complexity:
The time complexity of the code is O(log n). 
- Space Complexity:
The space complexity of the code is O(1).
### contains:
- Time Complexity:
The time complexity of the code is O(log n). 
- Space Complexity:
The space complexity of the code is O(1).
 

## Solution 

 ``` python 
  class BinarySearchTree(binary_tree):
    def __init__(self):
        self.root = None

    def add(self, value):
       
        if self.root is None:
            self.root = Tnode(value)
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left is None:
                        current.left = Tnode(value)
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = Tnode(value)
                        break
                    else:
                        current = current.right

    def contains(self, value):
        
        current = self.root
        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False
``` 