"""
A hash table is a data structure that allows for efficient lookup, insertion, and deletion of key-value pairs. It
works by using a hash function to compute an index into an array where the value is stored. The hash function takes
the key as input and returns an integer that represents the index into the array.

The main advantage of a hash table is its constant-time complexity for average-case lookups, insertions,
and deletions, which means that the time required to perform these operations is independent of the size of the hash
table. However, worst-case performance can be significantly worse, depending on the quality of the hash function and
the specific implementation of the hash table.

One common use case for hash tables is to implement associative arrays, where each key is associated with a value.
They are also used to implement sets, where the keys are the elements of the set and the values are not important.

In order to avoid collisions, where two keys hash to the same index in the array, hash tables typically use a
technique called chaining. This involves storing a linked list or other data structure at each index in the array,
and adding new key-value pairs to the list when there is a collision. Other techniques, such as open addressing,
can also be used to resolve collisions, but chaining is generally considered to be more efficient for most use cases.
"""


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        hash_value = self._hash(key)
        bucket = self.table[hash_value]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (k, value)
                return
        bucket.append((key, value))

    def get(self, key):
        hash_value = self._hash(key)
        bucket = self.table[hash_value]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(f"Key not found: {key}")

    def __repr__(self):
        items = []
        for bucket in self.table:
            for k, v in bucket:
                items.append(f"{k}: {v}")
        return "{" + ", ".join(items) + "}"



# create a new hash table with a size of 10
hash_table = HashTable(10)

# add some key-value pairs to the hash table
hash_table.put("apple", 1)
hash_table.put("banana", 2)
hash_table.put("orange", 3)

# retrieve values from the hash table
print(hash_table.get("apple"))  # output: 1
print(hash_table.get("banana"))  # output: 2
print(hash_table.get("orange"))  # output: 3

# update an existing key-value pair
hash_table.put("apple", 4)
print(hash_table.get("apple"))  # output: 4

# try to retrieve a key that doesn't exist
try:
    hash_table.get("grape")
except KeyError as e:
    print(str(e))  # output: 'Key not found: grape'

# print the contents of the hash table
print(hash_table)  # output: {apple: 4, banana: 2, orange: 3}
