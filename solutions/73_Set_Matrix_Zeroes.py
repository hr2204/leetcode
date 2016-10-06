# 73. Set Matrix Zeroes
# Difficulty: Medium
# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
#
# click to show follow up.
#
# Follow up:
# Did you use extra space?
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?
#


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        num_of_row = len(matrix)
        num_of_col = len(matrix[0])
        col_flag = [False] * num_of_col
        row_flag = [False] * num_of_row
        for row in matrix:
           for idx,num in enumerate(row):
               if num == 0:
                    col_flag[idx] = True

        for col_idx in range(num_of_col):
            for row_idx in range(num_of_row):
                if matrix[row_idx][col_idx] == 0:
                    row_flag[row_idx] = True
        print row_flag
        for idx,setZereo in enumerate(col_flag):
            if setZereo:
                for row_idx in range(num_of_row):
                    matrix[row_idx][idx] = 0

        for idx,setZereo in enumerate(row_flag):
            if setZereo:
                for col_idx in range(num_of_col):
                    matrix[idx][col_idx] = 0


if __name__ == '__main__':
    matrix = [[1,1,1,1],
              [1,0,1,1],
              [1,1,1,1]]
    Solution().setZeroes(matrix)
    for row in matrix:
        print row


    matrix = [[1,0]]
    Solution().setZeroes(matrix)
    for row in matrix:
        print row