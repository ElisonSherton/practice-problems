# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List

# Working Solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Keep track of all the upticks 
        upticks = []
        n = len(prices)
        
        # Get all the upticks -> O(n)
        for i in range(n - 1):
            nxt, cur = prices[i + 1], prices[i]
            if nxt > cur:
                upticks.append((cur, nxt))
        
        # If no single uptick, then return no profit
        if len(upticks) == 0:
            return 0

        # Create a container for all potential profits
        potential_profits = []
        
        # For each uptick
        # 1. Find lowest and buy
        # 2. Find highest to the right and sell if possible and add that to the potential profits list
        # 3. You're done checking from current lowest to the right so just chuck that portion away
        # 4. In the remaining portion, again get the lowest and see the highest to the right
        # 5. Keep doing this until you run out of all the upticks 
        # 6. Find the max of the potential profits
        while len(upticks) > 0:
            
            lowest, lowest_idx = upticks[0][0], 0
            
            for idx, (low, high) in enumerate(upticks):
                if low < lowest:
                    lowest = low
                    lowest_idx = idx
            
            best_sale = max([x[1] for x in upticks[lowest_idx:]])
            potential_profits.append(best_sale - lowest)
            upticks = upticks[:lowest_idx]
 
        return max(potential_profits)


# Incorrect solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Determine the lowest buy point
        n = len(prices)
        lowest_index, lowest_buy = -1, float("inf")

        for idx, element in enumerate(prices):
            if element < lowest_buy:
                lowest_index = idx
                lowest_buy = element
        
        if lowest_index == len(prices) - 1:
            return 0

        # Determine the highest sell point to the right of the lowest buy point
        highest_sell = lowest_buy
        highest_index = n + 1
        for j in range(lowest_index + 1, n):
            sell_price = prices[j]
            if sell_price > highest_sell:
                highest_sell = sell_price
                highest_index = j
        
        return highest_sell - lowest_buy