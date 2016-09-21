# 64. Minimum Path Sum  QuestionEditorial
# Difficulty: Medium
# Given a m x n grid filled with non-negative numbers, find a path from top left
# to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        if not grid:
            return res
        num_of_row = len(grid)
        num_of_col = len(grid[0])
        res = []
        res.append([grid[0][0]])
        for i in range(num_of_col):
            if i>0:
                res[0].append(res[0][i-1] + grid[0][i])
        for i in range(num_of_row):
            if i>0:
                res.append([0]*num_of_col)
                res[i][0] = res[i-1][0] + grid[i][0]
        for i in range(num_of_row):
            for j in range(num_of_col):
                if i>0 and j > 0:
                    res[i][j] = min(res[i-1][j],res[i][j-1]) + grid[i][j]
        return res[num_of_row-1][num_of_col-1]
if __name__ == '__main__':
    grid = [[1,1,1],
            [1,2,1]]
    print Solution().minPathSum(grid)