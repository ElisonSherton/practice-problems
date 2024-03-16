# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# Elegant version of the code below
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l, res = 0, 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            
            charSet.add(s[r])
            res = max(res, r - l + 1)
        
        return res

# Variable Length Sliding Window Solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0

        n = len(s)
        current_substring = ""
        longest_substring = ""
        window = set()

        # Iterate once over the entire string
        for R in range(n):
            
            # Extract the current element
            curr_element = s[R]

            # Window check, if curr element is not in window then we have a potential candidate for the longest substring
            if not curr_element in window:
                window.add(curr_element)
                current_substring += curr_element
                if len(current_substring) > len(longest_substring):
                    longest_substring = current_substring
                    
            else:
                # If the current element has occurred in the past, now move the L pointer to that position which is closest to R pointer and has the value as that of the current character
                closest_equal_index = L
                for i in range(L, R):
                    if s[i] == curr_element:
                        closest_equal_index = i

                # Remove those elements to the left of this index from the window
                window = window - set(s[L:closest_equal_index])

                # Modify the left pointer
                L = closest_equal_index + 1

                # Modify the current substring and subsequently the window here                            
                current_substring = s[L:(R + 1)]

        return len(longest_substring)            