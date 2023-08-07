'''
Medium
16.4K
468
Companies
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''

from typing import List
import unittest

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # declare a dictionary
        # iterate over the List of strs
        # create a newList to store sorted word,
        # check sortedword present in dictionary anagrams
        # assign sorted word to dict by appending word
        # if sortedword is not in dict, create a new key 'word' in anagrams
        # return list(anagrams.values())
        anagrams = {}
        for astr in strs:
            sorted_strs = ''.join(sorted(astr))
            if sorted_strs in anagrams:
                anagrams[sorted_strs].append(astr)
            else:
                anagrams[sorted_strs] = [astr]
        return list(anagrams.values())


sol = Solution()
results = sol.groupAnagrams(strs)
print(results)
'''

# Approach 2


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_char_count(astr: str) -> tuple:
            char_count = [0] * 26
            for char in astr:
                char_count[ord(char) - ord('a')] += 1
            return tuple(char_count)

        anagrams_dict = {}
        for mystr in strs:
            char_count_key = get_char_count(mystr)
            if char_count_key not in anagrams_dict:
                anagrams_dict[char_count_key] = []
            anagrams_dict[char_count_key].append(mystr)

        return list(anagrams_dict.values())

'''


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example1(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected_output = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        self.assertEqual(self.solution.groupAnagrams(strs), expected_output)

    def test_example2(self):
        strs = [""]
        expected_output = [[""]]
        self.assertEqual(self.solution.groupAnagrams(strs), expected_output)

    def test_example3(self):
        strs = ["a"]
        expected_output = [["a"]]
        self.assertEqual(self.solution.groupAnagrams(strs), expected_output)

    def test_example4_duplicate_anagrams(self):
        strs = ["eat", "tea", "ate", "tea", "bat", "tab", "act", "cat"]
        expected_output = [["eat", "tea", "ate", "tea"],
                           ["bat", "tab"], ["act", "cat"]]
        self.assertEqual(self.solution.groupAnagrams(strs), expected_output)

    def test_example5_empty_input(self):
        strs = []
        expected_output = []
        self.assertEqual(self.solution.groupAnagrams(strs), expected_output)


if __name__ == "__main__":
    unittest.main()
