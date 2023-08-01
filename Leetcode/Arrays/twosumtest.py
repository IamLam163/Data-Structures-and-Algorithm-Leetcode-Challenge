from typing import List


'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()

        for idx, val in enumerate(nums):
            adds_up = target - val

            if adds_up in seen:
                # Convert the tuples back to a list to match the function's return type
                return [nums.index(adds_up), idx]
            seen.add(val)

        return []


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


sol = Solution()

# Test case 1: Regular case with a valid result
nums1 = [2, 7, 11, 15]
target1 = 9
# The two numbers whose sum equals the target are 2 and 7 (index 0 and 1)
# Expected output: [0, 1]
# Explanation: nums[0] + nums[1] = 2 + 7 = 9 (target)
print(sol.twoSum(nums1, target1))

# Test case 2: No valid result
nums2 = [3, 6, 9]
target2 = 4
# There are no two numbers whose sum equals the target (4)
# Expected output: []
# Explanation: There are no numbers in the list whose sum is 4
print(sol.twoSum(nums2, target2))

# Test case 3: Negative numbers
nums3 = [-1, -2, -3, -4, -5]
target3 = -8
# The two numbers whose sum equals the target are -3 and -5 (index 2 and 4)
# Expected output: [2, 4]
# Explanation: nums[2] + nums[4] = -3 + -5 = -8 (target)
print(sol.twoSum(nums3, target3))

# Test case 4: Duplicate numbers with a valid result
nums4 = [3, 3, 2, 4]
target4 = 6
# The two numbers whose sum equals the target are 3 and 3 (index 0 and 1)
# Expected output: [0, 1]
# Explanation: nums[0] + nums[1] = 3 + 3 = 6 (target)
print(sol.twoSum(nums4, target4))
