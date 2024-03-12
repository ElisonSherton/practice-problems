# https://leetcode.com/problems/find-all-anagrams-in-a-string/

from typing import List

# Working Solution
class Solution:

    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns = len(s)
        np = len(p)

        if np > ns: return []

        # Keep a count of all the elements in target string p
        p_counts = {}
        for element in p:
            p_counts[element] = 1 + p_counts.get(element, 0)
        
        # Keep a running count of all the elements in source string s of window length np
        s_counts = {}
        for element in s[:np]:
            s_counts[element] = 1 + s_counts.get(element, 0)
        
        idxs = []
        left_pointer = 0
        while left_pointer <= ns - np:
            right_pointer = left_pointer + np
            
            # If you encounter an anagram and on sliding it is still an anagram, append all such indices to the list of valid anagrams
            if s_counts == p_counts:
                idxs.append(left_pointer)

            if right_pointer < ns:
                l_char, r_char = s[left_pointer], s[right_pointer]
                
                # Remove the character if it's count will drop to zero after this pass
                if s_counts[l_char] == 1: s_counts.pop(l_char)
                # Decrement the counter of the left encountered char by 1  
                else: s_counts[l_char] -= 1

                # Increment the counter of the right encountered char by 1
                s_counts[r_char] = 1 + s_counts.get(r_char, 0)
                left_pointer += 1
            else:
                break

        return idxs


# Trivial Solution
class Solution:

    def checkAnagram(self, s1, s2) -> bool:
        counts = {}

        for element in s1:
            counts[element] = 1 + counts.get(element, 0)
        
        for element in s2:
            c = counts.get(element, 0)
            if c == 0: return False
            counts[element] -= 1
        
        return True

    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Trivial Solution
        ns = len(s)
        np = len(p)

        start = 0
        end = ns - np + 1

        idxs = []
        for i in range(start, end):
            if self.checkAnagram(s[i: i + np], p):
                idxs.append(i)
        
        return idxs
