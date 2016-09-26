# 74. Search a 2D Matrix
# Difficulty: Medium
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# For example,
#
# Consider the following matrix:
#
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# Given target = 3, return true.


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        res = False
        if not matrix:
            return res
        num_row = len(matrix)
        num_col = len(matrix[0])
        if target < matrix[0][0] or target > matrix[num_row-1][num_col-1]:
            return False

        first_col = [row[0] for row in matrix]


    def binray_search_with_range(self,row,target):
        start, end = 0,len(row) - 1
        while start <= end:
            mid = start + (end - start)/2
            if row[mid]<=target<row[mid+1]:
                return mid
            elif target < row[mid]:
                end = mid
            else:
                start = mid
        return -1

    def binary_search(self,row,target):
        start, end = 0,len(row) - 1
        while start <= end:
            mid = start + (end - start)/2
            if target == row[mid]:
                return mid
            elif target < row[mid]:
                end = mid
            else:
                start = mid
        return -1

if __name__ == '__main__':
    matrix = [
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ]
    # print Solution().searchMatrix(matrix,3)
    print Solution().binray_search_with_range([1,2,3,4],4)