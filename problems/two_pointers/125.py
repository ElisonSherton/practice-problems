# https://leetcode.com/problems/valid-palindrome/description/

import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        valid = set(string.ascii_lowercase)
        valid = valid.union(set(string.digits))

        new_s = ""
        for element in s:
            e = element.lower()
            if e in valid:
                new_s = new_s + e

        L = 0
        R = len(new_s) - 1

        while L <= R:
            if new_s[L] != new_s[R]:
                return False
            L += 1
            R -= 1
        
        return True