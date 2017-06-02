#  542. 01 Matrix
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 5946
# Total Submissions: 18041
# Difficulty: Medium
# Contributors:
# Stomach_ache
# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
#
# The distance between two adjacent cells is 1.
# Example 1:
# Input:
#
# 0 0 0
# 0 1 0
# 0 0 0
# Output:
# 0 0 0
# 0 1 0
# 0 0 0
# Example 2:
# Input:
#
# 0 0 0
# 0 1 0
# 1 1 1
# Output:
# 0 0 0
# 0 1 0
# 1 2 1
# Note:
# The number of elements of the given matrix will not exceed 10,000.
# There are at least one 0 in the given matrix.
# The cells are adjacent in only four directions: up, down, left and right.


class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        row = len(matrix[0])
        col = len(matrix)

        checked = [[0 for i in xrange(row)] for j in xrange(col)]

        for col_idx in xrange(col):
            for row_idx in xrange(row):
                self.helper(matrix,row_idx,col_idx)

        return matrix


    def helper(self,matrix,i,j):
        if matrix[i][j] == 0:
            return
        # else:


            # for dir in [(1,0),(0,1),(-1,0),(0,-1)]:
            #     dx, dy = dir
            #     nx, ny = i + dx, j + dy
            #     if nx >= 0 and ny>=0 and nx < len(matrix[0]) and ny < len(matrix):





if __name__ == '__main__':
    input = [
        [0,0,0],
        [0,1,0],
        [1,1,1]
    ]
    print Solution().updateMatrix(input)
