"""
Binary search is an algorithm used to efficiently search for an element in a sorted list or array. The basic idea behind binary search is to divide the search range in 
half with each iteration, until the target element is found or it is determined that the element is not present in the list.

Here's how binary search works:
    1. Start with the middle element of the list.
    2. If the middle element is the target element, stop the search and return its index.
    3. If the middle element is greater than the target element, search the left half of the list.
    4. If the middle element is less than the target element, search the right half of the list.
    5. Repeat steps until the target element is found or it is determined that it is not present in the list.
    
Binary search has a time complexity of O(log n), which makes it very efficient for large lists. However, it only works on sorted lists, 
so if the list is unsorted, it must be sorted first.

Some notable examples where binary search is used include:
    1. Searching for a word in a dictionary - a dictionary is typically sorted alphabetically, so binary search can be used to quickly find a word.
    2. Searching for a number in a phonebook - similar to searching for a word in a dictionary, binary search can be used to quickly find a phone number in a sorted list.
    3. Finding an element in a large database - if the database is sorted, binary search can be used to quickly locate a specific record.
    4. Implementing autocomplete functionality in a text editor - when a user types a few characters, binary search can be used to quickly find a list of possible matches based on a sorted dictionary of words.
"""
import unittest

def binary_search(arr, target) -> str:
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return f"The number is at index {mid}"
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return "No such number exist!"


class TestBinarySearch(unittest.TestCase):
    def test_search_9(self):
        str = binary_search([1,2,3,4,5,6,7,8,9,10], 9)
        self.assertEqual("The number is at index 8", str)

if __name__ == "__main__":
    unittest.main()
