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


class Stack:
    def __init__(self, top=None):
        """
        Initializes a new instance of the Stack class.
        
        Args:
            top: The top node of the stack.
        """
        self.top = top

    def push(self, value):
        """
        Pushes a new element onto the stack.
        
        Args:
            value: The value to be pushed onto the stack.
        """
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        """
        Removes and returns the element at the top of the stack.
        
        Returns:
            The value of the element that was removed from the top of the stack.
        
        Raises:
            Exception: If the stack is empty.
        """
        if self.top == None:
            raise Exception("The stack is empty.")
        else:
            temp = self.top
            self.top = temp.next
            temp.next = None
            return temp.value

    def peek(self):
        """
        Returns the value of the element at the top of the stack without removing it.
        
        Returns:
            The value of the element at the top of the stack.
        
        Raises:
            Exception: If the stack is empty.
        """
        if self.top == None:
            raise Exception("The stack is empty.")
        else:
            return self.top.value

    def is_empty(self):
        """
        Checks if the stack is empty.
        
        Returns:
            True if the stack is empty, False otherwise.
        """
        return self.top == None

    def __str__(self):
        """
        Returns a string representation of the stack.
        
        Returns:
            A string representing the stack with elements separated by arrows.
        """
        current = self.top
        string = ""
        while current:
            string += f"{current.value}"
            string += " -> "
            current = current.next
        return string + "None"


if __name__ == "__main__":
    stack_01 = Stack()
    stack_01.push(1)
    stack_01.push(2)
    stack_01.push(3)
    stack_01.push(4)
    print(stack_01)
    print(stack_01.top.value)
