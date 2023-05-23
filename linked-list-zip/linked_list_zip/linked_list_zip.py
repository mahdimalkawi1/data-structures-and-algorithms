class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self.next = _next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def to_list(self):
        current = self.head
        lst = []
        while current:
            lst.append(current.value)
            current = current.next
        return lst

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

def zipLists(list1, list2):
    if list1.head is None:
        return list2
    if list2.head is None:
        return list1

    current1 = list1.head
    current2 = list2.head
    new_list = LinkedList()

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
