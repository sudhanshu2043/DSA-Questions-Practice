class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        frequency_s = {}
        frequency_t = {}

        # Count the frequency of characters in string s
        for char in s:
            frequency_s[char] = frequency_s.get(char, 0) + 1

        # Count the frequency of characters in string t
        for char in t:
            frequency_t[char] = frequency_t.get(char, 0) + 1

        # Compare the frequency dictionaries
        return frequency_s == frequency_t