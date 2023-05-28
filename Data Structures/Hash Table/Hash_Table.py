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
