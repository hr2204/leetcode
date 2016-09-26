# 240. Search a 2D Matrix II
# Difficulty: Medium
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# For example,
#
# Consider the following matrix:
#
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# Given target = 5, return true.
#
# Given target = 20, return false.

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        num_row = len(matrix)
        num_col = len(matrix[0])
        if target<matrix[0][0] or target>matrix[num_row-1][num_col-1]:
            return False
        idx_row = num_row -1
        idx_col = 0
        while idx_row >= 0 and idx_col < num_col:
            # print matrix[idx_row][idx_col]
            if matrix[idx_row][idx_col] == target:
                return True
            if matrix[idx_row][idx_col] > target:
                idx_row -= 1
            if matrix[idx_row][idx_col] < target:
                idx_col += 1
        return False
if __name__ == '__main__':
    matrix = [
      [1,   4,  7, 11, 15],
      [2,   5,  8, 12, 19],
      [3,   6,  9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]
    ]
    print Solution().searchMatrix([[]],5) == False

    print Solution().searchMatrix(matrix,5) == True
    print Solution().searchMatrix(matrix,20) == False