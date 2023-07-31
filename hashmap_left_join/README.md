# LEFT JOINs

Write a function that LEFT JOINs two hashmaps into a single data structure.


## Whiteboard Process

![ white board](./assets/Untitled%20(33).jpg)

## Approach & Efficiency

- Time Complexity:
The time complexity of the code is O(n). 
- Space Complexity:
The space complexity of the code is also O(n).
## Solution

``` python 
def left_join(hashTable1, hashTable2):
    '''
    A method to perform a left join between two hashtables.
    args: hashTable1, hashTable2
    output: a list of tuples of the form (key, value1, value2)
    '''
    output = [[key, hashTable1.get(key), hashTable2.get(key, None)] for key in hashTable1.keys()]
    return output

```

### [Tests](./tests/test_hashmap_left_join.py)


