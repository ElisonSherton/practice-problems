# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description/

# Much better solution
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        result = 0
        indices = {c: [-1, -1] for c in 'abcdefghijklmnopqrstuvwxyz'}

        for i in range(n):
            if indices[s[i]][0] == -1:
                indices[s[i]][0] = i
            else:
                indices[s[i]][1] = i

        for c, idx in indices.items():
            if idx[0] != -1 and idx[1] != -1:
                unique_chars = set(s[idx[0] + 1:idx[1]])
                result += len(unique_chars)

        return result

# Easy to understand but similar to the following solution
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        global_counts = {k: set() for k in list("abcdefghijklmnopqrstuvwxyz")}
        lhs_counts = {k: 0 for k in list("abcdefghijklmnopqrstuvwxyz")}
        
        for pos, element in enumerate(s):
            global_counts[element].add(pos)
        
        
        pals = set()
        for idx, element in enumerate(s):
            global_counts[element].discard(idx)

            for k in global_counts:
                if lhs_counts[k] > 0 and len(global_counts[k]) > 0:
                    pals.add(f"{k}{element}{k}")
            
            lhs_counts[element] = 1 + lhs_counts.get(element, 0)

            
        return len(pals)


# Slightly better -> Accepted solution
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        # Make one pass to compute the total counts
        total_counts = {}
        for element in s:
            total_counts[element] = 1 + total_counts.get(element, 0)
        
        # Maintain the counts of elements to my left
        lhs_counts = {}

        # Keep all the interesting palindromes in this set
        pals = set()
        for idx, element in enumerate(s):

            # Simulate RHS counts by making deletions to total counts
            total_counts[element] -= 1
            if total_counts[element] == 0: total_counts.pop(element)

            # Find same element to the right and to the left
            common_elems = lhs_counts.keys() & total_counts.keys()
            
            # Make the palindrome
            for e in common_elems:
                pals.add(f"{e}{element}{e}")
            
            lhs_counts[element] = 1 + lhs_counts.get(element, 0)

        return len(pals)


# Trivial Solution
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        lhs_set = set(s[0])
        pals = set()
        n = len(s)

        for idx, i in enumerate(s[1:], start = 1):
            rhs_set = set(list(s[idx+1:n]))
            ints = lhs_set & rhs_set
            for element in ints:
                pals.add(f"{element}{s[idx]}{element}")
            lhs_set.add(s[idx])

        return len(pals)
            