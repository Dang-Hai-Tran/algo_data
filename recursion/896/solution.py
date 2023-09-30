import unittest


# def isMonotonic(nums):
#     if all(nums[i] <= nums[i+1] for i in range(len(nums) - 1)):
#         return True
#     elif all(nums[i] >= nums[i+1] for i in range(len(nums) - 1)):
#         return True
#     else:
#         return False

def isMonotonic(nums):
    if (len(nums) <= 2):
        return True
    incr = decr = 0
    curr = nums[0]
    for num in nums:
        if num > curr:
            incr = 1
        if num < curr:
            decr = 1
        curr = num
        if incr == decr == 1:
            return False
    return True


class TestIsMonotonic(unittest.TestCase):
    def test_empty_list(self):
        self.assertTrue(isMonotonic([]))

    def test_increasing_sequence(self):
        self.assertTrue(isMonotonic([1, 2, 3, 4, 5]))

    def test_decreasing_sequence(self):
        self.assertTrue(isMonotonic([5, 4, 3, 2, 1]))

    def test_non_monotonic_sequence(self):
        self.assertFalse(isMonotonic([1, 3, 2, 4, 5]))

    def test_non_monotonic_middle(self):
        self.assertFalse(isMonotonic([5, 3, 2, 4, 1]))

    def test_non_monotonic_end(self):
        self.assertFalse(isMonotonic([1, 2, 3, 4, 2, 1]))

    def test_single_element(self):
        self.assertTrue(isMonotonic([100]))


if __name__ == '__main__':
    unittest.main()
