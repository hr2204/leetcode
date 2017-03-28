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



if __name__ == '__main__':
    input = [[1,0,1,0,0],
             [1,0,1,1,1],
             [1,1,1,1,1],
             [1,0,0,1,0]]
    print Solution().maximalSquare(input)