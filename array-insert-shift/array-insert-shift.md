# array-insert-shift 

Write a function called insertShiftArray which takes in an array and a value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.

## Whiteboard Process

![ white board](./assets/Untitled%20(8).jpg)

## Approach & Efficiency

## Solution

def insertShiftArray(arr, val):
    n = len(arr)
    mid = n // 2
    if n % 2 == 1:
        for i in range(mid+1, n):
            arr[i], val = val, arr[i]
        arr.append(val)
    else:
        for i in range(mid, n):
            arr[i], val = val, arr[i]
        arr.append(val)
    return arr
print(insertShiftArray([5,8,7,9,10],15))


if the array [2,4,6,-8] and the user input 5 the array will be [2,4,5,6,-8]