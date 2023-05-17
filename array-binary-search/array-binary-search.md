# BinarySearch

Write a function called BinarySearch which takes in 2 parameters: a sorted array and the search key. Without utilizing any of the built-in methods available to your language, return the index of the array’s element that is equal to the value of the search key, or -1 if the element is not in the array.


## Whiteboard Process

![ white board](./assets/Untitled%20(10).jpg)

## Approach & Efficiency

- Approach: We used while loop and if statement


- Time Complexity (Big O): O(log n)

    The Binary Search algorithm has a time complexity of O(log n) in the worst case, where 'n' is the number of elements in the input array. This is because the algorithm continuously divides the search space in half with each iteration, reducing the number of remaining elements to search. It achieves a logarithmic time complexity by discarding half of the remaining elements at each step.

- Space Complexity: O(1)

    The space complexity of the code is constant, O(1), because it uses a fixed amount of additional space regardless of the size of the input. The only variables used are left, right, mid, and key, which occupy a constant amount of memory. The space required does not increase with the input size, making it a constant space complexity.

## Solution

def BinarySearch(arr, key):

    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == key:
            return mid
        
        elif arr[mid] > key:
            right = mid - 1
        
        else:
            left = mid + 1
    
    return -1


   #### if the input is [4, 8, 15, 16, 23, 42], 15  the output will be 2 

