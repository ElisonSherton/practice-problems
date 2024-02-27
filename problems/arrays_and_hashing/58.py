# https://leetcode.com/problems/length-of-last-word/description/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Start with zero as the length of the current word
        word_len = 0
        s = s + " "

        # Keep a track of current word
        curr_word = None

        # Parse across the whole string from left to right

        for i in range(len(s)):
            if s[i] == " " or i == len(s):
                # Keep track of the current word and update it's length continuously to be the length of the current word
                if curr_word is None: continue
                word_len = len(curr_word)
                curr_word = None
            elif curr_word is None:
                curr_word = s[i]
            else:
                curr_word += s[i]
        
        # Eventual word's length is gonna be the last word's length
        return word_len
            

# Following solution is the same as above with the only difference that we start from the right and only look for the first maximal continual sequence of characters, so it should be slightly less time consuming although both the algorithms take O(n) complexity
class Solution2:
    def lengthOfLastWord(self, s: str) -> int:
        word_len = 0
        s = " " + s + " "
        curr_word = None
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " " or i == 0:
                if curr_word is None: continue
                word_len = len(curr_word)
                return word_len
            elif curr_word is None:
                curr_word = s[i]
            else:
                curr_word += s[i]
        
        return word_len
            


