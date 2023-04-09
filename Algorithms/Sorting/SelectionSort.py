"""
Selection Sort is a simple sorting algorithm that works by repeatedly finding the minimum element from an unsorted
portion of the array and moving it to the beginning of the array. This process is repeated until the entire array is
sorted.

Here are the basic steps:
    1. Find the minimum element in the unsorted sub-array.
    2. Swap the minimum element with the leftmost element in the unsorted sub-array, thus expanding the sorted sub-array
     by one element.
    3. Repeat steps 1 and 2 for the remaining unsorted sub-array, until the entire array is sorted.
    
Selection Sort has a time complexity of O(n^2) in both the best case and worst case scenarios. It is not a very
efficient algorithm for sorting large arrays, but it has the advantage of being simple to implement and requiring
minimal auxiliary space.

One of the main drawbacks of Selection Sort is that it is not stable, meaning that the relative order of equal elements
is not preserved during the sorting process. Another disadvantage is that it requires n-1 swaps in the worst case, where
 n is the size of the array, which can be a performance bottleneck for large arrays.

Overall, Selection Sort is a basic sorting algorithm that can be useful in certain situations, but for most practical
applications, more advanced sorting algorithms such as Quicksort or Merge Sort are preferred.
"""
import time
import unittest


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the minimum element in the unsorted part of the array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the minimum element with the first element of the unsorted part
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


class TestSelectionSort(unittest.TestCase):
    def setUp(self) -> None:
        self.small_arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        self.large_arr = list(range(10000, 0, -1))
        self.elapsed_time = 0

    def test_selection_sort_small_array(self):
        sorted_arr = selection_sort(self.small_arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_selection_sort_large_array(self):
        start_time = time.time()
        selection_sort(self.large_arr)
        end_time = time.time()
        self.elapsed_time = end_time - start_time
        self.assertGreaterEqual(self.elapsed_time, 2.0, print(f"Large array takes very long to finish: {self.elapsed_time}"))


if __name__ == '__main__':
    unittest.main()

