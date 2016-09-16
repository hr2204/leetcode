# 62. Unique Paths
# Difficulty: Medium
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
# How many possible unique paths are there?
#
#
# Above is a 3 x 7 grid. How many possible unique paths are there?
#
# Note: m and n will be at most 100.

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1
        res = []
        for i in range(m):
            if i == 0:
                res.append([1]*n)
            else:
                res.append([0]*n)


        for i in range(m):
            res[i][0] = 1

        for i in range(1,m):
            for j in range(1,n):
                res[i][j] = res[i][j-1] + res[i-1][j]
        return res[m-1][n-1]

if __name__ == '__main__':
    print Solution().uniquePaths(3,7)