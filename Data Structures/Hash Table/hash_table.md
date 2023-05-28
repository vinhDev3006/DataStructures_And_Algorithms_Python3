A hash table is a data structure that allows for efficient lookup, insertion, and deletion of key-value pairs. It
works by using a hash function to compute an index into an array where the value is stored. The hash function takes
the key as input and returns an integer that represents the index into the array.

The main advantage of a hash table is its constant-time complexity for average-case lookups, insertions,
and deletions, which means that the time required to perform these operations is independent of the size of the hash
table. However, worst-case performance can be significantly worse, depending on the quality of the hash function and
the specific implementation of the hash table.

<img style="display: block; 
           margin-left: auto;
           margin-right: auto;
           width: 100%;" 
      src="..\..\Assets\Images\hash_table_big_O.png" alt="hash table big O" width="700">

One common use case for hash tables is to implement associative arrays, where each key is associated with a value.
They are also used to implement sets, where the keys are the elements of the set and the values are not important.

In order to avoid collisions, where two keys hash to the same index in the array, hash tables typically use a
technique called chaining. This involves storing a linked list or other data structure at each index in the array,
and adding new key-value pairs to the list when there is a collision. Other techniques, such as open addressing,
can also be used to resolve collisions, but chaining is generally considered to be more efficient for most use cases.
