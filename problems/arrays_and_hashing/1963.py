# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/description/

class Solution:
    def minSwaps(self, s: str) -> int:
        
        extra_closing_count = 0
        max_extra_count = 0

        for element in s:
            if element == "[":
                extra_closing_count -= 1
            elif element == "]":
                extra_closing_count += 1
            
            max_extra_count = max(max_extra_count, extra_closing_count)
        
        return (max_extra_count + 1) // 2