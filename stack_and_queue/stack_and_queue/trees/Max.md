# Find the Maximum Value in a Binary Tree



## Whiteboard Process

![ white board](./assetss/Untitled%20(25).jpg)


## Approach & Efficiency
- Time Complexity:
The time complexity of the code is O(n). 
- Space Complexity:
The space complexity of the code is O(1).


## Solution 

 ``` python 
 def max_value(self):
        """ find and returns the maximum value in a binary tree."""

        self.max = self.root.value
        def _walk(root):
            if root.value > self.max:
                self.max = root.value       
            if root.left:
                _walk(root.left)
            if root.right:
                _walk(root.right)
        _walk(self.root)
        return self.max
``` 