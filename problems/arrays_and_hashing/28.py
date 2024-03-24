# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

# Optimized Solution: KMP Algorithm 

# Trivial Solution
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        haystack_size = len(haystack)
        needle_size = len(needle)

        if needle_size > haystack_size:
            return -1

        for i in range(0, haystack_size - needle_size + 1):
            to_compare = haystack[i: i + needle_size]
            if to_compare == needle:
                return i
        
        return -1
            