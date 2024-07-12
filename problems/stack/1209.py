# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/




# Working solution but takes too long
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
                
        deleted = True
        original_s = s

        # Go through the string until there is no consecutive k duplicates left
        while True:
            to_delete = []

            L = 0
            n = len(s)

            # Iterate over the string until the last but k indices
            while L < n - k + 1:
                R = L + k
                sub_str = s[L:R]
                # Make a list of the indices which have k consecutive repeated alphabets
                if len(set(sub_str)) == 1:
                    to_delete.append(L)
                    L = R
                else:
                    L = L + 1

            # If nothing is to be deleted till now, break out of the loop
            if not to_delete:
                break
            # If there is, then delete it and get the string s ready for the next pass
            else:
                new_s = ""
                prev = 0
                for element in to_delete:
                    new_s = new_s + s[prev:element]  
                    prev = element + k
                new_s = new_s + s[prev:]
                s = new_s

        return s