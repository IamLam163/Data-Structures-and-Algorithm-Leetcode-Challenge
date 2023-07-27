# Intuition

<!-- Describe your first thoughts on how to solve this problem. -->

My first thought to solving this problem was a bruteforce approach which is to just iterate over the entire list, and compare each element of the array to the next. Although this worked, it didn't take into account a List with a vast number of elements, it also didn't take into account an unsorted list.

##### First Approach

```
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == num[j]:
                    return True
        return False
```

<!-- Describe your approach to solving the problem. -->

The first approach has a time complexity of $$O(n^2)$$ because it utilizes two for loops to compare two elements which is very inefficient because as the array grows larger, the run time also increases. Hence, I had to refactor the code to be more efficient.

---

##### Second Approach

```
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
                if nums[i] == nums[i + 1]:
                    return True
        return False
```

The second approach was more efficient than the first because the dominant operation was sorting the list and the approach utilised a single for loop. The sort method in python uses the Timsort algorithm which has a time complexity of O(n log n) which is more time efficient than the first approach.

# Complexity

- Time complexity: **$$O(n log n)$$**
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: **$$O(1)$$** This is beause the sorting operation was performed in place i.e no new space was allocated for the List in memory.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

Though this approach passed all test cases, a more efficient method to solve this problem is by utilising a Dictionary i,e a Hash map

# Code
