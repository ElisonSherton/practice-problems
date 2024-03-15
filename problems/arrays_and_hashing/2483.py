# https://leetcode.com/problems/minimum-penalty-for-a-shop/

# Working solution
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # Find the penalty if shop closes at zeroth hour
        penalty = 0
        for element in customers:
            if element == "Y": penalty += 1

        # Find the total length of customers
        n = len(customers)

        # Find penalty if shop closes at ith hour
        penalties = [penalty]
        min_penalty = float("inf")

        for i in range(1, n + 1):
            # Keep track of min penalty every iteration 
            if penalty < min_penalty:
                min_penalty = penalty

            # Compute penalty at ith hour
            if customers[i - 1] == "Y":
                penalty -= 1
            else:
                penalty += 1
            
            penalties.append(penalty)

        # If the final penalty is less than the penalties so far, need to acount for that
        if penalty < min_penalty:
            min_penalty = penalty

        # Return the first index where we find the min_penalty computed from above
        for idx, p in enumerate(penalties):
            if p == min_penalty:
                return idx
        
        return 0