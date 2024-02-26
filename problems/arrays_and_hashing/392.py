# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_slider = 0

        # If t is smaller than s, no point in checking any further
        if len(t) < len(s):
            return False

        # Move from left to right along both sequences s and t and check if you exhaust out on the sequence t
        for s_slider in range(len(s)):
            to_compare = s[s_slider]
            while True:
                if t_slider < len(t) and to_compare == t[t_slider]:
                    t_slider += 1
                    break
                t_slider += 1
                if t_slider >= len(t):
                    return False
        
        return True
