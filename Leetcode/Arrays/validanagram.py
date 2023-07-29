'''
# Approach 1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sortS = sorted(s)
        sortT = sorted(t)
        return sortS == sortT

'''

'''
# Approach 2


class solution:
    def isanagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return false

        hashs, hasht = {}, {}
        for item in range(len(s)):
            hashs[s[item]] = 1 + hashs.get(s[item], 0)
            hasht[t[item]] = 1 + hasht.get(t[item], 0)
        return hashs == hasht

'''

# Approach 3


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        def getCharFreq(word):
            freq = {}
            for char in word:
                freq[char] = 1 + freq.get(char, 0)
            return freq

        frequencyS = getCharFreq(s)
        frequencyT = getCharFreq(t)
        return frequencyS == frequencyT


# Test cases
test_cases = [
    # Test case with anagrams
    ("anagram", "nagaram", True),

    # Test case with non-anagrams
    ("rat", "car", False),

    # Test case with anagrams having the same characters but different counts
    ("listens", "silent", False),

    # Test case with empty strings
    ("", "", True),

    # Test case with single-character strings (anagrams)
    ("a", "a", True),

    # Test case with single-character strings (non-anagrams)
    ("a", "b", False),

    # Test case with strings of different lengths (non-anagrams)
    ("hello", "word", False),

    # Test case with strings containing spaces and special characters (anagrams)
    ("debit card", "bad credit", True),

    # Test case with strings containing spaces and special characters (non-anagrams)
    ("debit card", "bad debt", False),

    # Unicode Test Cases

    # Anagrams with accented characters
    ("\u00E1\u00E9\u00ED", "\u00ED\u00E9\u00E1", True),
    # Non-anagrams with Unicode characters
    ("\u0041\u0041\u0041", "\u0041\u0042\u0041", False),
    # Anagrams with Arabic characters
    ("\u0623\u0622\u0621", "\u0621\u0623\u0622", True),
    # Anagrams with Greek characters
    ("\u0391\u0392\u0393", "\u0393\u0392\u0391", True),
    # Anagrams with Chinese characters
    ("\u4E16\u754C\u60A8", "\u60A8\u754C\u4E16", True),
    ("\u092F\u0939\u0948", "\u0948\u0939\u092F", True)
]

sol = Solution()

for s, t, expected_result in test_cases:
    result = sol.isAnagram(s, t)
    assert result == expected_result, f"Test failed! Input: {s}, {t}, Expected: {expected_result}, Got: {result}"

print('All test cases passed Successfully!')
