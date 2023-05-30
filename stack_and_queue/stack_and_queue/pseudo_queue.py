try:
    from stack import Stack
except ImportError:
    from stack_and_queue.stack import Stack

class PseudoQueue:
    """
    A class representing a pseudo queue that uses two stacks internally to implement enqueue and dequeue operations.
    """
    def __init__(self):
        """
        Initializes a new instance of the PseudoQueue class.
        """
        self.stack_1 = Stack()  
        self.stack_2 = Stack()  

    def enqueue(self, value):
        """
        Adds the specified value to the pseudo queue.

        Args:
            value: The value to be enqueued.
        """
        self.stack_1.push(value)

    def dequeue(self):
        """
        Removes and returns the first element from the pseudo queue.

        Raises:
            Exception: If the queue is empty.
        """
        if self.stack_1.is_empty():
            raise Exception("The queue is empty")

        if self.stack_2.is_empty():
            while not self.stack_1.is_empty():
                self.stack_2.push(self.stack_1.pop())

            self.stack_2.pop()

            while not self.stack_2.is_empty():
                self.stack_1.push(self.stack_2.pop())

    def __str__(self):
        """
        Returns a string representation of the pseudo queue.

        Returns:
            A string representation of the pseudo queue.
        """
        elements = []
        while not self.stack_1.is_empty():
            elements.append(self.stack_1.pop())

        for element in reversed(elements):
            self.stack_1.push(element)

        string = " -> ".join(str(element) for element in elements)
        return string


if __name__ == "__main__":
    q = PseudoQueue()
    q.enqueue("hi")
    q.enqueue("welcome")
    q.enqueue("bye")
    q.dequeue()
    print(q)
