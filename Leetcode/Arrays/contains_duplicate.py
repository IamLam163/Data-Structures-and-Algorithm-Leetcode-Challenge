from typing import List

'''
# Approach 0
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        newhash = {}
        for i in range(len(nums)):
            if i in newhash:
                return True
            newhash[i] = True
        return False
'''

'''
# Approach 1
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
                if nums[i] == nums[i + 1]:
                    return True
        return False
'''

# Approach 2


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = {}  # Dictionary to store visited elements
        for num in nums:
            if num in visited:
                return True
            visited[num] = True
        return False


# Test cases
test_cases = [
    # Test case with duplicates
    ([1, 2, 3, 4, 5, 2], True),

    # Test case without duplicates
    ([1, 2, 3, 4, 5], False),

    # Test case with negative numbers
    ([1, -2, 3, -4, 5, -2], True),

    # Test case with empty list
    ([], False),

    # Test case with large input
    ([i for i in range(1, 10001)] + [10000], True),

    # Test case with all duplicates
    ([5] * 10, True),

    # Test case with floating-point numbers
    ([1.5, 2.0, 3.5, 1.5], True),
]

# Create an instance of the Solution class
sol = Solution()

# Perform the tests
for nums, expected_result in test_cases:
    result = sol.containsDuplicate(nums)
    assert result == expected_result, f"Test failed! Input: {nums}, Expected: {expected_result}, Got: {result}"

print("All test cases passed successfully!")
