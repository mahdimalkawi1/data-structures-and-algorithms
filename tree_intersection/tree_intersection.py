from functools import reduce
from operator import add

class Node:
  '''
  A class represent a node in a linked list or other data structure each node has two main componenet the value of the node and the reference to the next node.
  args: value
  return : nothing
  '''
  def __init__(self, value):
      self.next=None 
      self.value=value



class LinkedList:
    '''
    what : A class representing a singly linked list data structure
    '''
    def __init__(self):
        self.head = None


    def insert (self, value):
        '''
        insert a new node with the given value at the begining of     the linked list.
        args: value
        output : none
        
        '''
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node


class HashTable:
  '''
  what : data structure that store key-value pairs of data using buckets to increace data accessing efficiency 
  
  '''
  def __init__(self,size=1024):
    self.__size=size
    self.__buckets=[None] *size
    self.keys = []
    
  
  def __hash(self,key):
    '''
    A method to return the hash code of the given key
    arg : key
    output: hash code of the key(index)
    '''
    # code = 0
   
    # for char in key:
    #   code += ord(str(char)) # * weight
    # code *= 255
    # code = code % 1024
    # return code
    return reduce(add, [ord(str(char)) for char in str(key)]) * 283 % self.__size
    # return sum([ord(str(char)) for char in key]) * 283 % self.__size

  
    
  def set(self,key,value):
    '''
    Set a key-value pair in the bucket, handling collisions as              needed.
    Arguments:
    key : The key to be hashed and used as the identifier for the           value.
    value : the value that is aassociated with the key
    Returns: None
    '''
    index = self.__hash(key)
    if self.__buckets[index] is None:
      ll = LinkedList()
      self.__buckets[index] = ll
     
    self.__buckets[index].insert([key,value])
    self.keys.append(key)
    
    

 

  def get(self,key):
    '''
    Retrieve the value with the given key from the hashtable
    arg : key
    return : value or None 
    '''
    index=self.__hash(key)
    bucket = self.__buckets[index]
    if bucket is not None : 
      curr = bucket.head
      while curr :
        if curr.value[0] == key :
          return curr.value[1]
        curr = curr.next  
    return None  
    
    

  def has(self, key):
    '''
    A method to check if the given key exist in the hashtable.
    arg: key
    output: boolean
    '''
    # index=self.__hash(key)
    # bucket = self.__buckets[index]
    # if bucket is not None : 
    #   curr = bucket.head
    #   while curr :
    #     if curr.value[0] == key :
    #       return True
    #     curr = curr.next  
    #   return False  
    if self.get(key):
      return True
    return False  

    

  def keyss(self):
    '''
    args : none
    Returns a list of all the  keys present in the Hashtable.
    '''
    return self.keys
  
  def check_collision (self,key):
    index=self.__hash(key)
    bucket = self.__buckets[index]
    if bucket is not None : 
      curr = bucket.head
      count=0
      while curr :
        count+=1
        curr = curr.next
      if count>1:
          return True 
      
    return False
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
    
def tree_intersection(tree1,tree2):
    """
    Find the intersection of two binary search trees.

    Args:
        tree1: The first binary search tree.
        tree2: The second binary search tree.

    Returns:
        list: A list containing the values of the intersection of the two binary search trees.
    """
    hash_table = HashTable()
    nodes = tree1.post_order()
    intersection = []
    for node in nodes:
      hash_table.set(node,node)

    nodes = tree2.post_order()
    for node in nodes:
      if hash_table.has(node):
         intersection.append(node)
    return intersection

      
   
    
if __name__ == "__main__":
    # Create two binary search trees
    tree1 = BinarySearchTree()
    tree2 = BinarySearchTree()

    # Add elements to the first tree
    tree1.add(5)
    tree1.add(2)
    tree1.add(8)
    tree1.add(1)
    tree1.add(3)

    # Add elements to the second tree
    tree2.add(7)
    tree2.add(2)
    tree2.add(9)
    tree2.add(1)
    tree2.add(4)

    # Find common values in both trees
    common_values = tree_intersection(tree1, tree2)
    print("Common values:", common_values)  # Output: [1, 2]

