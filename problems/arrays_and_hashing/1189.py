# https://leetcode.com/problems/maximum-number-of-balloons/submissions/1195271103/

# Smarter Solution
# Keep a track of how many times each individual character can be reused to form the word balloon
# Return the minimum number of times that this could be done
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        char_count = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}
        per_instance_occurrence = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}

        for element in text:
            if element in char_count:
                char_count[element] += 1
        
        balloons_count = 10**5
        for k in char_count:
            c = char_count[k] // per_instance_occurrence[k]
            balloons_count = min(balloons_count, c)        
        
        return balloons_count

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        balloons_count = 0
        char_count = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}

        # Maintain a track of the characters of the element balloon
        for element in text:
            if element in char_count:
                char_count[element] += 1

        # Count how many balloon characters appeared in the word
        while True:
            for k in ["b", "a", "l", "o", "n"]:
                v = char_count[k]
                if (k in ["b", "a", "n"]) and (v > 0):
                    char_count[k] -= 1
                elif (k in ["l", "o"]) and (v > 1):
                    char_count[k] -= 2
                else:
                    return balloons_count 
            balloons_count += 1   
        