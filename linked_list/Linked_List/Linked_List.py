class Node : #value next
    def __init__(self, value,_next=None):
        self.value = value
        self.next = _next



class linked_list:
    def __init__(self,head=None):
        self.head = head


    def insert (self, value) : 
         new_node = Node(value)
         new_node.next = self.head
         self.head = new_node.value

         
    def includes(self, value):
     current = self.head
     while current:
        if current.value == value:
            return True
        current = current.next
     return False

    def to_string(self):
        current = self.head
        string = ""
        while current:
            string += "{" + f"{current.value} " + "}" + "-> "
            current = current.next
        string += " None "
        return string




