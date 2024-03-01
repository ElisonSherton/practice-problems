# https://leetcode.com/problems/group-anagrams/description/
# There is a more optimal solution to this -> Simply use a hashmap as number of characters is limited from a - z
# Key -> xxxxxx...26 times where each x represents count of abcdef....
# Values are a list of the strings themselves
# Link to optimal solution: https://www.youtube.com/watch?v=vzdNOK2oB2E
from typing import List

class Solution:

    def isAnagram(self, s1, s2):
        if len(s1) != len(s2):
            return False
        
        if (len(s1) == len(s2)) and (len(s1) == 0):
            return True
        
        s1_counts = {}
        for element in s1:
            try: 
                s1_counts[element] += 1
            except KeyError as e:
                s1_counts[element] = 1
        
        for element in s2:
            if not element in s1_counts:
                return False
            elif s1_counts[element] == 0:
                return False
            else:
                s1_counts[element] -= 1
        
        return True
                
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Group all indices by their length
        # This will reduce the number of comparisons to be done in subsequent step
        # O(m . n) -> m = len(strs), n = avg string length
        index_groups = {}
        for idx, s in enumerate(strs):
            k = len(s)
            if k in index_groups: index_groups[k].add(idx)
            else: index_groups[k] = {idx}

        # Check for anagrams within groups of same length
        # O(m**2 * n) time complexity 
        groups = []
        for all_indices in index_groups.values():
            while len(all_indices) > 0:
                
                # Within this group of same length strings, create a container to accumulate the sub-group of anagrams
                # Take a random element and search for it's anagrammic words
                # Once you are done then repeat the process with the remaining words in this group until you exhaust this entire group
                curr_group = []
                curr_idx = all_indices.pop()
                curr_element = strs[curr_idx]
                
                curr_group.append(curr_element)

                visited = []
                for j in all_indices:
                    compare_element = strs[j]  
                    if self.isAnagram(compare_element, curr_element):
                        curr_group.append(compare_element)
                        visited.append(j)
                
                for element in visited:
                    all_indices.remove(element)

                groups.append(curr_group)
        
        return groups