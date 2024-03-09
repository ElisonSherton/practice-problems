# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

from typing import List

# Much simpler solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices) - 1):
            max_profit += max(0, prices[i + 1] - prices[i])        
        return max_profit

# Working solution but fails for last test case on leetcode
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)

        # Check if the entire series is descending in order
        descending = True
        for i in range(n - 1):
            if prices [i + 1] > prices[i]:
                descending = False
                break
        if descending:
            return 0

        # If there are some upticks then go ahead and check for best combination
        profit_map = {i: 0 for i in range(n)}

        for i in range(n - 2, -1, -1):
            buy_price = prices[i]

            # If tomorrow's price is same as today's price, calcs will stay the same hence no need to recompute
            if buy_price == prices[i + 1]:
                profit_map[i] = profit_map[i + 1]
                continue

            profit_candidates = [0]
            
            # Check for each sale price what is the profit
            for j in range(i + 1, n):
                sale_price = prices[j]
                future_profit = profit_map[j]
                # Buy the share only if it makes profit and append the future profit to it
                profit_candidates.append(max(0, sale_price - buy_price) + future_profit)
            
            # Now you can assign max profit from all candidates to the current day in profit map
            profit_map[i] = max(profit_candidates)
        
        return max(profit_map.values())