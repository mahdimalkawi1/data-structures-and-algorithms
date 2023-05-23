# zipLists


## Whiteboard Process
![ white board](./linked_list_zip/assets/Untitled%20(16).jpg)


## Approach & Efficiency
- Time Complexity:
This is because the code iterates through both lists simultaneously using the while loop, appending the values from each list to the new linked list. In the worst case, it visits each node in both lists once, resulting in a linear time complexity.

- Space Complexity:
This is because the code creates a new linked list (new_list) to store the alternated nodes from the input lists. The space required by new_list will be proportional to the number of nodes in the longer list.

## Solution 

 ``` python
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
```

- list1:
{1} -> {3} -> {2} -> null
- list2:
{5} -> {9} -> {4} -> null
- output:
{1} -> {5} -> {3} -> {9} -> {2} -> {4} -> null