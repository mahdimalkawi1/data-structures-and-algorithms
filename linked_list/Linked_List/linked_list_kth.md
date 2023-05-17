# linked-list-kth


## Whiteboard Process
![ white board](./assetss/Untitled%20(13).jpg)


## Approach & Efficiency
- Time Complexity:
The time complexity of the code is O(n^2)

- Space Complexity:
The space complexity of the code is also O(n).
## Solution 

 
  def kth  (self,k):
        current=self.head
        list=[]
        while current != None:
            list.insert(0, current.value)
            current=current.next 

        if k<=len(list):
            return(list[k]) 
        else:
            raise Exception("Index out of range.")

- Input:
head -> {1} -> {3} -> {8} -> {2} -> X
- Output:
 2