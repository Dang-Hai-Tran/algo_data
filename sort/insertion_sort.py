from typing import TypeVar
import unittest

T = TypeVar('T')


def insertionSort(l: list[T]) -> list[T]:
    for i in range(1, len(l)):
        key = l[i]
        j = i - 1
        while j >= 0 and l[j] > key:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key
    return l


class InsertionSortTest(unittest.TestCase):
    def test_insertion_sort(self):
        # Test case 1: sorted list
        l = [1, 2, 3, 4, 5]
        self.assertEqual(insertionSort(l), [1, 2, 3, 4, 5])

        # Test case 2: reverse sorted list
        l = [5, 4, 3, 2, 1]
        self.assertEqual(insertionSort(l), [1, 2, 3, 4, 5])

        # Test case 3: empty list
        l = []
        self.assertEqual(insertionSort(l), [])

        # Test case 4: list with duplicate values
        l = [3, 2, 5, 2, 1]
        self.assertEqual(insertionSort(l), [1, 2, 2, 3, 5])

        # Test case 5: list with negative values
        l = [-4, -2, -6, -1, -3]
        self.assertEqual(insertionSort(l), [-6, -4, -3, -2, -1])

        # Test case 6: list with mixed positive and negative values
        l = [4, -2, 0, -1, 3]
        self.assertEqual(insertionSort(l), [-2, -1, 0, 3, 4])

        l = ['b', 'e', 'c', 'f', 'd', 'a']
        self.assertEqual(insertionSort(l), ['a', 'b', 'c', 'd', 'e', 'f'])


if __name__ == '__main__':
    unittest.main()
