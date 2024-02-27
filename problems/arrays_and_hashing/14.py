# https://leetcode.com/problems/longest-common-prefix/description/
from typing import List

class Solution:

    def commonPrefix(self, s1: str, s2: str):
        # Given two strings, find the longest common string starting from left
        longest_common = ""
        
        for e1, e2 in zip(list(s1), list(s2)):
            if e1 == e2:
                longest_common += e1
            else:
                return longest_common

        return longest_common

    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Take the first string here
        current = longest_common = strs[0]
        
        # Compare and keep track of longest common substring across all words from index 1 onwards
        for s in strs[1:]:
            longest_common = self.commonPrefix(current, s)
            current = longest_common

        return longest_common