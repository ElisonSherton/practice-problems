# https://leetcode.com/problems/valid-sudoku/description/
from typing import List

class Solution:

    def check_unique(self, arr: List[str]) -> bool:
        nums = set()
        for element in arr:
            if element != ".":
                if element in nums:
                    return False
                nums.add(element)
        return True

    def check_row(self, board: List[List[str]], row_num: int) -> bool:
        row = board[row_num]
        return self.check_unique(row)
    
    def check_column(self, board: List[List[str]], col_num: int) -> bool:
        col = [x[col_num] for x in board]
        return self.check_unique(col)

    def check_box(self, board: List[List[str]], box_num: int) -> bool:

        # Extract all the elements of a particular box in the sudoku grid
        start_row = 3 * (box_num // 3)
        start_col = 3 * (box_num % 3)

        arr = []
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                arr.append(board[i][j])

        # Check for presence of duplicates
        return self.check_unique(arr) 

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            row_check = self.check_row(board, i)
            if not row_check: return False

            col_check = self.check_column(board, i)
            if not col_check: return False
            
            box_check = self.check_box(board, i)
            if not box_check: return False
        
        return True
            