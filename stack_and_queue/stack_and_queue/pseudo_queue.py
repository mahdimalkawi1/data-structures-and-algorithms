try:
    from stack import Stack
except ImportError:
    from stack_and_queue.stack import Stack

class PseudoQueue:
    def __init__(self):
        self.stack_1 = Stack()  
        self.stack_2 = Stack()  

    def enqueue(self, value):
        self.stack_1.push(value)

    def dequeue(self):
        if self.stack_1.is_empty():
            raise Exception("The queue is empty")

        if self.stack_2.is_empty():
            while not self.stack_1.is_empty():
                self.stack_2.push(self.stack_1.pop())

            self.stack_2.pop()

            while not self.stack_2.is_empty():
                self.stack_1.push(self.stack_2.pop())

    def __str__(self):
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
