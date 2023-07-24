# hashmap repeated word

Write a function called repeated word that finds the first word to occur more than once in a string

## Whiteboard Process

![ white board](./assets/Untitled%20(30).jpg)

## Approach & Efficiency

- Time Complexity:
The time complexity of the code is O(n). 
- Space Complexity:
The space complexity of the code is also O(n).
## Solution

``` python 
def repeated_word(input_string):

    if not isinstance(input_string, str):
        raise Exception("Input is not a string")

    words = input_string.lower().split()
    word_table = HashTable()

    for word in words:
        clean_word = ''.join(i for i in word if i.isalnum())

        if clean_word:
            if word_table.has(clean_word):
                return clean_word
            word_table.set(clean_word, True)

    return None
```

### [Tests](./tests/test_hashmap_repeated_word.py)


