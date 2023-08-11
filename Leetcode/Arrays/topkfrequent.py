'''
347. Top K Frequent Elements
Medium
15.5K
542
Companies
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.


Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''


from typing import DefaultDict, List
from collections import Counter
import unittest


# Approach 1
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = DefaultDict(int)
        for num in nums:
            mydict[num] += 1
        return sorted(mydict, key=lambda value: mydict[value], reverse=True)[:k]


# Approach 2
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = {}
        for num in nums:
            if num not in mydict:
                mydict[num] = 0
            mydict[num] += 1
        return sorted(mydict, key=lambda value: mydict[value], reverse=True)[:k]

'''

'''
# Approach 3
# The shortest and easiest :)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = Counter(nums)
        return [item[0] for item in mydict.most_common(k)]

'''


class TestTopKFrequent(unittest.TestCase):
    def test_example_case(self):
        solution = Solution()
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        expected_output = [1, 2]
        self.assertEqual(solution.topKFrequent(nums, k), expected_output)

    def test_empty_list(self):
        solution = Solution()
        nums = []
        k = 3
        expected_output = []
        self.assertEqual(solution.topKFrequent(nums, k), expected_output)

    def test_single_element_list(self):
        solution = Solution()
        nums = [5]
        k = 1
        expected_output = [5]
        self.assertEqual(solution.topKFrequent(nums, k), expected_output)

    def test_k_greater_than_unique_elements(self):
        solution = Solution()
        nums = [1, 2, 3, 4, 5]
        k = 10
        expected_output = [1, 2, 3, 4, 5]
        self.assertEqual(solution.topKFrequent(nums, k), expected_output)

    def test_duplicate_elements(self):
        solution = Solution()
        nums = [3, 3, 3, 3, 2, 2, 1]
        k = 2
        expected_output = [3, 2]
        self.assertEqual(solution.topKFrequent(nums, k), expected_output)


if __name__ == '__main__':
    unittest.main()
