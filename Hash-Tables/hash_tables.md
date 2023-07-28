# LAB - Class 30
## Task: Hash Table Implementation
### Author: Mahdi Malkawi


## Approach & Efficiency

### Efficiency

- **Time complexity**: set, get, has, and keys methods: In the worst case, when there are many collisions and all keys hash to the same index, the time complexity of these methods can be O(n), where n is the number of key-value pairs in the hashtable. On average, when there are fewer collisions, the time complexity approaches O(1).
Hash Function: The time complexity of the hash function is O(k), where k is the length of the key. Since the keys' length is usually small and constant, the hash function can be considered as O(1).
Space Complexity:

- **Space complexity**: The space complexity of the Hashtable is O(m + n), where m is the size of the hashtable (number of buckets), and n is the number of key-value pairs in the hashtable. In our implementation, the size is fixed at 100 (m = 100), and the space used for each key-value pair is constant (O(1)).
The space complexity of the hash function is also O(1) since it uses a fixed number of operations and does not depend on the input size.

## 3. Solution

this implementation of the Hashtable class is efficient for small to moderate-sized datasets and provides constant-time lookups in the average case when there are fewer collisions. However, for larger datasets and potential high collision rates, more advanced hash table implementations, like chaining with balanced trees or open addressing, may offer better performance.