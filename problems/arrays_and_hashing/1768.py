# https://leetcode.com/problems/merge-strings-alternately/description/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        w1_ptr = w2_ptr = 0
        result = ""

        while True:
            if (w1_ptr >= len(word1)) or (w2_ptr >= len(word2)):
                break
            
            result += word1[w1_ptr] + word2[w2_ptr]

            w1_ptr += 1
            w2_ptr += 1
        
        # This works because of the string slicing beauty in python
        result += word1[w1_ptr:] + word2[w2_ptr:]

        return result