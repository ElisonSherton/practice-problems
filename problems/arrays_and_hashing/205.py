# https://leetcode.com/problems/isomorphic-strings/description/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_len, t_len = len(s), len(t)
        t_encountered = set()

        # If the two strings are of different length, they cant be isomorphic
        if s_len != t_len:
            return False

        # Keep a key-value store for mapping s-chars to t-chars
        st_map = {}

        # Look at all the elements one by one
        for i in range(s_len):
            s_char, t_char = s[i], t[i]
            
            # Check if the char already exists in the store
            if s_char in st_map:
                # If yes, then check if the character in t is same as the value mapped in the store
                if st_map[s_char] != t_char:
                    return False
            else:
                # Check if the character in t is already encountered, if yes; this will be a many to one set which is not permitted
                if t_char in t_encountered:
                    return False
                st_map[s_char] = t_char
                t_encountered.add(t_char)

        # If all checks are passed, that means strings are isomorphic
        return True        