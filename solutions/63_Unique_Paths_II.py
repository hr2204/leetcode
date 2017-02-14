# 63. Unique Paths II
#
# Difficulty: Medium
# Contributors: Admin
# Follow up for "Unique Paths":
#
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
#
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
#
# For example,
# There is one obstacle in the middle of a 3x3 grid as illustrated below.
#
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# The total number of unique paths is 2.


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0

        row = len(obstacleGrid)
        col = len(obstacleGrid[0])

        res = [[0] * col for _ in range(row)]

        for i in range(col):
            if obstacleGrid[0][i] != 1:
                res[0][i] = 1
            else:
                break

        for i in range(row):
            if obstacleGrid[i][0] != 1:
                res[i][0] = 1
            else:
                break
        for row_idx in range(1,row):
            for col_idx in range(1,col):
                if obstacleGrid[row_idx][col_idx] == 1:
                    res[row_idx][col_idx] = 0
                else:
                    res[row_idx][col_idx] = res[row_idx-1][col_idx] + res[row_idx][col_idx-1]

        return res[row - 1][col - 1]


if __name__ == '__main__':
    input = [
        [0, 0, 0]
    ]
    print Solution().uniquePathsWithObstacles(input)
