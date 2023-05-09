# reverseArray 
Write a function called reverseArray which takes an array as an argument. Without utilizing any of the built-in methods available to your language, return an array with elements in reversed order.

## Whiteboard Process

![ white board](../array-reverse/assets/Untitled%20(7).jpg)

## Approach & Efficiency

## Solution

def reverseArray(arr):
    reversed_arr = []
    
    for i in range(len(arr)-1, -1, -1):
        reversed_arr.append(arr[i])
        
    return reversed_arr

input_str = input("Enter values: ")

input_arr = input_str.split(",")

output_arr = reverseArray(input_arr)

for element in output_arr:
    print(element)


if the input is [1, 2, 3, 4, 5, 6] the output will be [6, 5, 4, 3, 2, 1]
