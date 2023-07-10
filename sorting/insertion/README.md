# Insertion Sort


## Code in Python:

``` python 
def insertion_sort(input):
    sorted_array = [input[0]] 
    for i in range(1, len(input)):
        insert(sorted_array, input[i])  
    return sorted_array

def insert(sorted_array, value):
    i = 0
    while value > sorted_array[i]:
        i += 1
    while i < len(sorted_array):
        temp = sorted_array[i]
        sorted_array[i] = value
        value = temp
        i += 1

    sorted_array.append(value)

sample_array = [8, 4, 23, 42, 16, 15]
sorted_result = insertion_sort(sample_array)
print("Sorted array:", sorted_result)


```

### sample array: [8,4,23,42,16,15]

### Step 1:

- Initially, the sorted array is empty, and the first element of the input array is 8.
- The first element is directly inserted into the sorted array since there are no elements to compare it with.
- The sorted array after the first iteration: [8]

### Step 2:

- The second element of the input array is 4.
- We compare 4 with the elements in the sorted array from left to right.
- Since 4 is smaller than 8, we insert it before 8.
- The sorted array after the second iteration: [4, 8]

### Step 3:

- The third element of the input array is 23.
- We compare 23 with the elements in the sorted array from left to right.
- 23 is greater than 4, so we move to the next element, which is 8.
- 23 is greater than 8, so we move to the next element, which is the end of the sorted array.
- Since we have reached the end of the sorted array, we insert 23 at the end.
- The sorted array after the third iteration: [4, 8, 23]

### Step 4:

- The fourth element of the input array is 42.
- We compare 42 with the elements in the sorted array from left to right.
- 42 is greater than 4, so we move to the next element, which is 8.
- 42 is greater than 8, so we move to the next element, which is 23.
- 42 is greater than 23, so we move to the next element, which is the end of the sorted array.
- Since we have reached the end of the sorted array, we insert 42 at the end.
- The sorted array after the fourth iteration: [4, 8, 23, 42]
### Step 5:

- The fifth element of the input array is 16.
- We compare 16 with the elements in the sorted array from left to right.
- 16 is greater than 4, so we move to the next element, which is 8.
- 16 is greater than 8, so we move to the next element, which is 23.
- 16 is smaller than 23, so we insert 16 before 23.
- The sorted array after the fifth iteration: [4, 8, 16, 23, 42]
### Step 6:

- The sixth element of the input array is 15.
- We compare 15 with the elements in the sorted array from left to right.
- 15 is greater than 4, so we move to the next element, which is 8.
- 15 is smaller than 8, so we insert 15 before 8.
- The sorted array after the sixth iteration: [4, 8, 15, 16, 23, 42]

#### After processing the entire input array, we have the final sorted array: [4, 8, 15, 16, 23, 42].


### sample array: [5,12,7,5,5,7]

### Step 1:

- Initially, the sorted array is empty, and the first element of the input array is 5.
- The first element is directly inserted into the sorted array since there are no elements to compare it with.
- The sorted array after the first iteration: [5]

### Step 2:

- The second element of the input array is 12.
- We compare 12 with the elements in the sorted array from left to right.
- 12 is greater than 5, so we move to the next element, which is the end of the sorted array.
- Since we have reached the end of the sorted array, we insert 12 at the end.
- The sorted array after the second iteration: [5, 12]

### Step 3:

- The third element of the input array is 7.
- We compare 7 with the elements in the sorted array from left to right.
- 7 is greater than 5, so we move to the next element, which is the end of the sorted array.
- Since we have reached the end of the sorted array, we insert 7 at the end.
- The sorted array after the third iteration: [5, 12, 7]

### Step 4:

- The fourth element of the input array is 5.
- We compare 5 with the elements in the sorted array from left to right.
- 5 is equal to 5, so we insert 5 before the current element (5) to maintain the relative order.
- The sorted array after the fourth iteration: [5, 5, 12, 7]

### Step 5:

- The fifth element of the input array is 5.
- We compare 5 with the elements in the sorted array from left to right.
- 5 is equal to 5, so we insert 5 before the current element (5) to maintain the relative order.
- The sorted array after the fifth iteration: [5, 5, 5, 12, 7]

### Step 6:

- The sixth element of the input array is 7.
- We compare 7 with the elements in the sorted array from left to right.
- 7 is greater than 5, so we move to the next element, which is 5.
- 7 is greater than 5, so we move to the next element, which is the end of the sorted array.
- Since we have reached the end of the sorted array, we insert 7 at the end.
- The sorted array after the sixth iteration: [5, 5, 5, 7, 12]

#### After processing the entire input array, we have the final sorted array: [5, 5, 5, 7, 12].


## Efficency

### Time Complexity: O(n^2)
- The time complexity of the Insertion Sort algorithm implemented in the code is O(n^2) because the basic operation of this algorithm is comparison

### Space Complexity: O(1)
- The space complexity of the code is O(1), indicating constant space usage. This is because the algorithm performs in-place sorting, modifying the original array without utilizing any additional space that grows with the input size.

