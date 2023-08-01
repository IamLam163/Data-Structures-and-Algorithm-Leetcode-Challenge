import unittest
from typing import List

# Approach 1

'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}

        for idx, val in enumerate(nums):
            match = target - val

            if match in mydict:
                return [mydict[match], idx]

            mydict[val] = idx

        return []


'''
# Approach 2


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()

        for idx, val in enumerate(nums):
            match = target - val

            if match in seen:
                # Convert the tuples back to a list to match the function's return type
                return [nums.index(match), idx]
            seen.add(val)

        return []


# Tests
class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_regular_case(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected_output = [0, 1]
        self.assertEqual(self.sol.twoSum(nums, target), expected_output)

    def test_no_valid_result(self):
        nums = [3, 6, 9]
        target = 4
        expected_output = []
        self.assertEqual(self.sol.twoSum(nums, target), expected_output)

    def test_negative_numbers(self):
        nums = [-1, -2, -3, -4, -5]
        target = -8
        expected_output = [2, 4]
        self.assertEqual(self.sol.twoSum(nums, target), expected_output)

    def test_duplicate_numbers(self):
        nums = [3, 3, 2, 4]
        target = 6
        expected_output = [0, 1]
        self.assertEqual(self.sol.twoSum(nums, target), expected_output)


if __name__ == '__main__':
    unittest.main()
