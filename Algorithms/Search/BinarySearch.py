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