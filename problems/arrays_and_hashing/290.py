# https://leetcode.com/problems/word-pattern/description/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        p_s_map = {}
        s_p_map = {}

        s = s.split(" ")
        p = list(pattern)

        # If the number of chars in pattern don't match the number of words in s, we cannot establish a bijection
        if len(p) != len(s):
            return False
        

        for p_char, s_char in zip(p, s):
            # Check for a violation of bijection while mapping elements of p -> s and elements of s -> p 
            if p_char in p_s_map:
                if s_char != p_s_map[p_char]:
                    return False
            else:
                p_s_map[p_char] = s_char
            
            if s_char in s_p_map:
                if p_char != s_p_map[s_char]:
                    return False
            else:
                s_p_map[s_char] = p_char
        
        return True