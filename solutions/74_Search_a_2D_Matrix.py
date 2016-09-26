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
        row_idx = self.binray_search_with_range(first_col,target)
        if row_idx!= -1:
            return self.binary_search(matrix[row_idx],target)
        return False

    def binray_search_with_range(self,nums,target):
        if len(nums) == 0:
            return 0

        start, end = 0, len(nums) - 1
        # first position >= target
        while start + 1 < end:
            mid = (start + end) / 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid

        if nums[start] == target:
            return start
        if nums[start] > target:
            return start - 1
        if nums[end] == target:
            return end
        if nums[end] > target:
            return end - 1
        return len(nums) - 1

    def binary_search(self,row,target):
        start, end = 0,len(row) - 1

        while start + 1 < end:
            mid = start + (end - start)/2
            if row[mid] == target:
                return True
            if target > row[mid]:
                start = mid
            if target < row[mid]:
                end = mid
        if row[start] == target or row[end] == target:
            return True
        return False

if __name__ == '__main__':
    matrix = [
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ]
    print Solution().searchMatrix([[1,3,5]],4) == False

    print Solution().searchMatrix([[1,3,5]],1) == True

    print Solution().searchMatrix([[1]],1) == True

    print Solution().searchMatrix([[1,3]],2) == False

    print Solution().searchMatrix(matrix,3) == True
    # print Solution().binray_search_with_range([1,10,23],3)
    # print Solution().binary_search([1,3,5,7],3)