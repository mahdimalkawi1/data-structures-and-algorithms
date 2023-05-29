# Implement a Queue using two Stacks.


## Whiteboard Process
![ white board](./assetes/Untitled%20(18).jpg)
![ white board](./assetes/Untitled%20(19).jpg)



## Approach & Efficiency
##### enqueue 
- Time Complexity:
The time complexity of the code is O(1). 
- Space Complexity:
The space complexity of the code is also O(1).
##### dequeue 
- Time Complexity:
The time complexity of the code is O(n). 
- Space Complexity:
The space complexity of the code is also O(n). 

## Solution 

 ``` python 
 def enqueue(self, value):
        self.stack1.push(value)

    def dequeue(self):

        if self.stack1.is_empty() :
            raise Exception("the queue is empty")

        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())

            self.stack2.pop()
            while not self.stack2.is_empty():
                self.stack1.push(self.stack2.pop())
        return self.stack1
``` 

- Input:
[10]->[15]->[20]	
- Output:
[5]->[10]->[15]->[20]

- Input:
[5]->[10]->[15]->[20]
- Output:
[5]->[10]->[15]