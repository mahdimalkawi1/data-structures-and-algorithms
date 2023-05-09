# BinarySearch

Write a function called BinarySearch which takes in 2 parameters: a sorted array and the search key. Without utilizing any of the built-in methods available to your language, return the index of the array’s element that is equal to the value of the search key, or -1 if the element is not in the array.


## Whiteboard Process

![ white board](./assets/Untitled%20(6).jpg)

## Approach & Efficiency


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

