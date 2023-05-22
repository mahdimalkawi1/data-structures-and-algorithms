class Node : #value next
    def __init__(self, value,_next=None):
        self.value = value
        self.next = _next



class linked_list:
    def __init__(self,head=None):
        self.head = head


    def insert(self, value):
     new_node = Node(value)
     if self.head is None: 
        self.head = new_node
     else:
         new_node.next = self.head
         self.head = new_node

         
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
            string += "{ " + f"{current.value} " + "}" + "-> "
            current = current.next
        string += " None "
        return string
    
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_before(self, value, new_value):
        new_node = Node(new_value)
        if self.head is None:
            return
        if self.head.value == value:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        while current.next:
            if current.next.value == value:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def insert_after(self, value, new_value):
        new_node = Node(new_value)
        current = self.head
        while current:
            if current.value == value:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def kth  (self,k):
        current=self.head
        list=[]
        while current != None:
            list.insert(0, current.value)
            current=current.next 

        if k < 0:
            raise Exception ("Negative value not accepted.")
        elif k<=len(list):
            return(list[k]) 
        else:
            raise Exception("Index out of range.")
        
    def zipLists(self, list1, list2):
        """
        Zips two linked lists together by alternating nodes from each list.

        Args:
            list1: The first linked list.
            list2: The second linked list.

        Returns:
            A new linked list containing the nodes alternated from both input lists.
        """
        if list1.head is None:
            return list2
        if list2.head is None:
            return list1

        current1 = list1.head
        current2 = list2.head
        new_list = linked_list()

        while current1 and current2:
            new_list.append(current1.value)
            new_list.append(current2.value)
            current1 = current1.next
            current2 = current2.next

        if current1:
            while current1:
                new_list.append(current1.value)
                current1 = current1.next
        elif current2:
            while current2:
                new_list.append(current2.value)
                current2 = current2.next

        return new_list


    

