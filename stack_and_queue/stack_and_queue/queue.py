class Node:
    def __init__(self, value=None, next=None):
        """
        Initializes a new instance of the Node class.
        
        Args:
            value: The value to be stored in the node.
            next: The reference to the next node.
        """
        self.value = value
        self.next = next


class Queue:
    def __init__(self, front=None, back=None):
        """
        Initializes a new instance of the Queue class.
        
        Args:
            front: The first node in the queue.
            back: The last node in the queue.
        """
        self.front = front
        self.back = back

    def enqueue(self, value):
        """
        Adds a new element to the back of the queue.
        
        Args:
            value: The value to be added to the queue.
        """
        node = Node(value)
        if self.front == None:
            self.front = node
            self.back = node
        else:
            self.back.next = node
            self.back = node 

    def dequeue(self):
        """
        Removes and returns the element at the front of the queue.
        
        Returns:
            The value of the element that was removed from the queue.
        
        Raises:
            Exception: If the queue is empty.
        """
        if self.front == None:
            raise Exception("The Queue is empty.")
        else:
            temp = self.front
            self.front = temp.next
            temp.next = None
            return temp.value
        
    def peek(self):
        """
        Returns the value of the element at the front of the queue without removing it.
        
        Returns:
            The value of the element at the front of the queue.
        
        Raises:
            Exception: If the queue is empty.
        """
        if self.front == None:
            raise Exception("The Queue is empty.")
        else:
            return self.front.value
         
    def is_empty(self):
        """
        Checks if the queue is empty.
        
        Returns:
            True if the queue is empty, False otherwise.
        """
        return self.front == None
    
    def __str__(self):
        """
        Returns a string representation of the queue.
        
        Returns:
            A string representing the queue with elements separated by arrows.
        """
        current = self.front
        string = ""
        while current:
            string += f"{current.value}"
            string += " -> "
            current = current.next
        return string + "None"   


if __name__ == "__main__":
    q = Queue()
    q.enqueue("hi")
    q.enqueue("welcome")
    q.enqueue("bye")
    print(q)
    print(q.front.value)
    print(q.back.value)
    print("deleted element is ", q.dequeue()) 
    print(q)
