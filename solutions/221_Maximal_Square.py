# 221. Maximal Square
# Difficulty: Medium
# Contributors: Admin
# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
#
# For example, given the following matrix:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# Return 4.

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0 if matrix[i][j] == '0' else 1 for j in xrange(n)] for i in xrange(m)]

        for i in xrange(1,m):
            for j in xrange(1,n):
                if matrix[i][j] != '0':
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
        return max([max(i) for i in dp]) ** 2





if __name__ == '__main__':
    input = [['1','0','1','0','0'],
             ['1','0','1','1','1'],
             ['1','1','1','1','1'],
             ['1','0','0','1','0']]
    print Solution().maximalSquare(input)