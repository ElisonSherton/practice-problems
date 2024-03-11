# https://leetcode.com/problems/grid-game/description/
from typing import List

# Further optimizing the space complexity
class Solution:

    def gridGame(self, grid: List[List[int]]) -> int:
        
        # Keep the top sum precomputed
        top_sum = sum(grid[0])
        n = len(grid[0])

        top_running_sum = 0
        bottom_running_sum = 0
        result = float("inf")

        # Iterate over the entire row from left to right
        for i in range(n):
            # Keep track of top running sum
            top_running_sum += grid[0][i]
            
            # Compute the blue reward at current position 
            blue_reward = max(top_sum - top_running_sum, bottom_running_sum)
            
            # Keep track of bottom running sum but with a lag of one timestep
            bottom_running_sum += grid[1][i]

            # If the current reward is smaller than any of the rewards computed till now, then set that as the result
            result = min(blue_reward, result)
        
        return result

# Smart Solution
class Solution:

    def gridGame(self, grid: List[List[int]]) -> int:
        
        # Keep the top sum precomputed
        top_sum = sum(grid[0])
        n = len(grid[0])

        top_running_sum = 0
        bottom_running_sum = 0
        blue_rewards = []

        # Iterate over the entire row from left to right
        for i in range(n):
            # Keep track of top running sum
            top_running_sum += grid[0][i]
            
            # Compute the blue reward at current position 
            blue_reward = max(top_sum - top_running_sum, bottom_running_sum)
            
            # Keep track of bottom running sum but with a lag of one timestep
            bottom_running_sum += grid[1][i]

            # Accumulate how much blue bot would earn if the red bot switched position from zeroth to second row at column position i
            blue_rewards.append(blue_reward)
        
        # Since we want the minimum reward of blue, compute the min of the entire reward array created above
        return min(blue_rewards)

# Trivial Solution
class Solution:

    def getAllPathRewards(self, grid: List[List[int]]) -> List:

        second_row_total = sum(grid[1])

        # Keep two pointers for maintaining a prefix sum
        first_row_sum = second_row_sum = 0

        # Iterate from left to right
        n = len(grid[0])
        rewards = [0] * n
        for position in range(n):

            # Find out the current cell rewards
            current_r1_reward = grid[0][position]
            current_r2_reward = grid[1][position]

            # Find out the current path reward
            total_reward = first_row_sum + current_r1_reward + (second_row_total - second_row_sum)
            rewards[position] = total_reward

            first_row_sum += current_r1_reward
            second_row_sum += current_r2_reward

        return rewards

    def getOptimalPath(self, rewards: List[int]) -> List[int]:

        # Find out where the max sum lies and rearrange the matrix accordingly
        max_reward = 0; switch_position = 0
        for idx, element in enumerate(rewards):
            if element > max_reward:
                max_reward = element
                switch_position = idx

        return max_reward, switch_position

    def red_trampled_configuration(self, grid: List[List[int]], switch_position:int) -> List[List[int]]:
        n = len(grid[0])
        trampled_configuration = [[0 for i in range(n)] for _ in range(2)]
        for i in range(n):
            if i < switch_position:
                trampled_configuration[1][i] = grid[1][i]
            elif i > switch_position:
                trampled_configuration[0][i] = grid[0][i]
        return trampled_configuration

    def gridGame(self, grid: List[List[int]]) -> int:

        n = len(grid[0])

        blue_rewards = []
        for i in range(n):
            # Assume red switches rows at this position
            red_traversed_grid = self.red_trampled_configuration(grid, i)
            # print(red_traversed_grid, i)
            # print()

            # Blue Traversal
            curr_pos_blue_rewards = self.getAllPathRewards(red_traversed_grid)
            curr_pos_best_blue_reward, curr_pos_best_blue_switch = self.getOptimalPath(curr_pos_blue_rewards)

            blue_rewards.append(curr_pos_best_blue_reward)

        # print(f"{blue_rewards=}")

        return min(blue_rewards)
