# linked-list-insertions


## Whiteboard Process
![ white board](./assets/Untitled%20(9).jpg)
![ white board](./assets/Untitled%20(14).jpg)
![ white board](./assets/Untitled%20(15).jpg)



## Approach & Efficiency
- Time Complexity:
In the worst case scenario, where the new node is appended at the end of the linked list, the method needs to traverse the entire linked list to find the last node. Therefore, the time complexity is O(n), where n is the number of nodes in the linked list.

- Space Complexity:
The space complexity of the append method is O(1) since it only requires a constant amount of additional space to create the new node and variables new_node and current. The space used does not grow with the size of the linked list.
## Solution 

 
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node 

- Input:
head -> {1} -> {3} -> {2} -> X
- Output:
head -> {1} -> {3} -> {2} -> {5} -> X