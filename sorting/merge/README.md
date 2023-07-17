# Merge Sort

## Code in Python:

``` python 
def merge_sort(arr):
    n = len(arr)

    if n > 1:
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        merge(left, right, arr)

def merge(left, right, arr):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
```

### sample array: [8,4,23,42,16,15]

### Step 1:
- Initially, the input array is [8, 4, 23, 42, 16, 15].
- The Mergesort algorithm is called with the entire array.

### Step 2:
- The length of the array is greater than 1, so the array is divided into two halves: [8, 4, 23] and [42, 16, 15].

### Step 3:
- The Mergesort algorithm is recursively called for both halves.

### Step 4:
For the left half [8, 4, 23]:

- The length of the left half is greater than 1, so it is further divided into [8] and [4, 23].
- The Mergesort algorithm is recursively called for both subarrays.
- For the subarray [8], no further division is possible, so it remains the same.
- For the subarray [4, 23], it is further divided into [4] and [23].
- Again, no further division is possible for these subarrays.
- The Merge algorithm is called to merge the sorted subarrays [4] and [23] into [4, 23].

### Step 5:
For the right half [42, 16, 15]:

- The length of the right half is greater than 1, so it is further divided into [42] and [16, 15].
- The Mergesort algorithm is recursively called for both subarrays.
- For the subarray [42], no further division is possible, so it remains the same.
- For the subarray [16, 15], it is further divided into [16] and [15].
- Again, no further division is possible for these subarrays.
- The Merge algorithm is called to merge the sorted subarrays [16] and [15] into [15, 16].
### Step 6:
- Finally, the Merge algorithm is called to merge the sorted subarrays [4, 23] and [15, 16] of the left and right halves, respectively, into the final sorted array [4, 15, 16, 23, 42].


#### After processing the entire input array, we have the final sorted array: [4, 15, 16, 23, 42].

## Efficency

### Time Complexity: O(n log n)

- The time complexity of the Merge Sort algorithm is O(n log n) because the algorithm recursively divides the array into smaller subarrays until the base case is reached, and then merges the sorted subarrays. 

### Space Complexity: O(n)

- The space complexity of the Merge Sort algorithm is O(n) because the algorithm requires additional space to store the divided subarrays and the merged result during the recursive calls. 
