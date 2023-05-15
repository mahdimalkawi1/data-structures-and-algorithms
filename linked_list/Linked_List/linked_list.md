# linked-list


## Whiteboard Process
![ white board](./assetss/Untitled%20(11).jpg)


## Approach & Efficiency
- Time Complexity:
The time complexity of the code is O(1). The reason is that regardless of the size of the linked list, the code performs a constant number of operations. It creates a new node, updates the next pointer of the new node, and updates the head pointer. These operations do not depend on the size of the linked list.

- Space Complexity:
The space complexity of the code is also O(1). The reason is that the amount of memory used by the code does not depend on the input size or the size of the linked list. It creates a single new node to hold the new value, but this does not change based on the input size. The memory usage remains constant.
## Solution 

 
    def insert(self, value):
     new_node = Node(value)
     if self.head is None: 
        self.head = new_node
     else:
         new_node.next = self.head
         self.head = new_node

- Input:
head -> {1} -> {3} -> {2} -> X
- Output:
 {5}(head) -> {1} -> {3} -> {2} -> X