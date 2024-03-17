# https://leetcode.com/problems/valid-palindrome-ii/description/

# Working solution but not so efficient
class Solution:
    def validPalindrome(self, s: str) -> bool:

        L = 0
        R = len(s) - 1

        # Once you can forgive and once you can afford to make a choice
        # If that choice goes wrong, go back to the state where you made the choice and make a different choice and hereforth no forgiveness will be given
        forgive = True
        state = (L, R)

        while L <= R:
            if s[L] == s[R]:
                pass
            elif forgive:
                if state != (0, len(s) - 1):
                    forgive = False
                    L, R = state
                else:
                    # By default always drop the right character
                    # Keep this in the state variable, so that when we backtrack, we will drop the left character
                    state = (L, R + 1)
                    L = L - 1
            else:
                return False
            L = L + 1
            R = R - 1
            

        return True    

# Did not work because only one choice was made
class Solution:
    def validPalindrome(self, s: str) -> bool:

        L = 0
        R = len(s) - 1
        forgive = True

        while L <= R:
            if s[L] == s[R]:
                pass
            elif forgive:
                forgive = False
                # Make a decision of which character to delete
                # Be greedy i.e. delete that char which makes me a palindrome now
                if s[L] == s[R - 1]:
                    L = L - 1
                elif s[R] == s[L + 1]:
                    R = R + 1
                else:
                    L = L - 1
            else:
                return False
            L = L + 1
            R = R - 1
            

        return True    