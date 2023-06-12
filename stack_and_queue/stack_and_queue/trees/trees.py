try:
    from queue import Queue
except ImportError:
    from stack_and_queue.queue import Queue


class Tnode:
    
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class binary_tree:
    """
        Perform breadth-first traversal on the binary tree.

        Returns:
            list: A list containing the values of the binary tree in breadth-first order.
        """
    def __init__(self):
        self.root = None
        self.max = None

    def breadth_first(self):
        if not self.root:
            return self.root

        output = []
        queue = Queue()
        queue.enqueue(self.root)

        while not queue.is_empty():

            front = queue.dequeue()
            output.append(front.value)

            if front.left:
                queue.enqueue(front.left)
            if front.right:
                queue.enqueue(front.right)

        return output

    def pre_order(self):
        """
        Perform pre-order traversal on the binary tree.

        Returns:
            list: A list containing the values of the binary tree in pre-order traversal.
        """
        arr = []

        def _walk(root):
            # root
            arr.append(root.value)

            # left
            if root.left:
                _walk(root.left)

            # right
            if root.right:
                _walk(root.right)

        _walk(self.root)
        return arr

    def in_order(self):
        """
        Perform in-order traversal on the binary tree.

        Returns:
            list: A list containing the values of the binary tree in in-order traversal.
        """
        arr = []

        def _walk(root):
            # left
            if root.left:
                _walk(root.left)

            # root
            arr.append(root.value)

            # right
            if root.right:
                _walk(root.right)

        _walk(self.root)
        return arr

    def post_order(self):
        """
        Perform post-order traversal on the binary tree.

        Returns:
            list: A list containing the values of the binary tree in post-order traversal.
        """
        arr = []

        def _walk(root):
            # left
            if root.left:
                _walk(root.left)

            # right
            if root.right:
                _walk(root.right)

            # root
            arr.append(root.value)

        _walk(self.root)
        return arr
    
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
    

class BinarySearchTree(binary_tree):
    def __init__(self):
        self.root = None

    def add(self, value):
        """
        Add a value to the binary search tree.

        The value is added to the appropriate position in the binary search tree according to its ordering.

        Args:
            value: The value to be added to the binary search tree.
        """
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
        """
        Check if a value is present in the binary search tree.

        The method searches for the given value in the binary search tree and returns True if found, False otherwise.

        Args:
            value: The value to check for containment in the binary search tree.

        Returns:
            bool: True if the value is present in the binary search tree, False otherwise.
        """

        current = self.root
        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False


if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(20)
    tree.add(50)
    tree.add(30)
    tree.add(40)
    tree.add(60)

    # print(tree.pre_order())
    # print("###############")
    # print(tree.in_order())
    # print("###############")
    # print(tree.post_order())
    print("###############")
    print(tree.max_value())
    

