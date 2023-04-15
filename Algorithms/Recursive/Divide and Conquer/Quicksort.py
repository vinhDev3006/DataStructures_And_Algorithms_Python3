"""
Quicksort is a widely used sorting algorithm that has an average time complexity of O(n log n), making it one of
the fastest general-purpose sorting algorithms. It was developed by Tony Hoare in 1959 and has since become one of
the most popular and efficient sorting algorithms in use today.

The basic idea behind Quicksort is to divide an unsorted array into two smaller sub-arrays, one with elements smaller
than a chosen pivot and one with elements larger than the pivot. This process is repeated recursively on each of the
sub-arrays until the sub-arrays have at most one element each, at which point the sub-arrays are merged to produce a
sorted array.

One of the key strengths of Quicksort is that it is an in-place sorting algorithm, meaning it does not require
additional memory to perform the sorting operation. This makes it particularly useful in applications where memory
usage is a concern.

One potential disadvantage of Quicksort is that its performance can degrade to O(n^2) in the worst case,
when the selected pivot is either the largest or smallest element in the array. To avoid this, sophisticated pivot
selection techniques are used, such as choosing a random pivot or selecting the median element as the pivot.

Despite this potential weakness, Quicksort remains a popular and effective sorting algorithm due to its simplicity,
speed, and in-place nature. It is commonly used in computer science courses and programming interviews,
and is a standard library sorting algorithm in many programming languages.
"""


import random
import timeit
import unittest

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

class TestQuicksort(unittest.TestCase):
    def test_quicksort(self):
        test_arr = [3, 2, 1, 5, 4, 6, 9, 8, 0, 7]
        expected_output = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(quicksort(test_arr), expected_output)

if __name__ == '__main__':
    # Generate a random array of size 1,000,000 for testing
    test_arr = [random.randint(0, 10000) for _ in range(1000000)]

    # Time the Quicksort operation
    start_time = timeit.default_timer()
    quicksort(test_arr)
    end_time = timeit.default_timer()
    run_time = end_time - start_time
    print(f"Quicksort took {run_time:.6f} seconds to sort a list of size 1000000")

    # Run the unittests
    unittest.main()