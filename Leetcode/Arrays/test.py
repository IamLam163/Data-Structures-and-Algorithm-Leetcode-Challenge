from typing import List

'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = {}  # Dictionary to store visited elements
        for num in nums:
            if num in visited:
                return True
            visited[num] = True
        return False
'''


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for element in nums:
            if element in dict:
                return True
            dict[element] = True
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

# Perform the tests(test_cases)
for nums, expected_result in test_cases:
    result = sol.containsDuplicate(nums)
    assert result == expected_result, f"Test failed! Input: {nums}, Expected: {expected_result}, Got: {result}"

print("All test cases passed successfully!")
