# https://leetcode.com/problems/pascals-triangle/description/

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        sol = [[1], [1,1]]

        if numRows == 1:
            return sol[:1]
        elif numRows == 2:
            return sol
        else:
            for i in range(3, numRows + 1):
                r = [1]
                prev_row = sol[-1]
                for e1, e2 in zip(prev_row[:-1], prev_row[1:]):
                    r.append(e1 + e2)
                r.append(1)
                sol.append(r)
        return sol
