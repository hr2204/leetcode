# 120. Triangle  QuestionEditorial Solution  My Submissions
# Total Accepted: 82820
# Total Submissions: 261299
# Difficulty: Medium
# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
#
# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
# Note:
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

import math
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        res = 0
        row_sum = []
        if not triangle:
            return
        if len(triangle) == 1:
            return triangle[0][0]
        row_sum.append(triangle[0][0]+triangle[1][0])
        row_sum.append(triangle[0][0]+triangle[1][1])

        if len(triangle) == 2:
            return min(row_sum)
        for level in range(2,len(triangle)):
            row = triangle[level]
            temp_row = [0] * (level + 1)
            for idx,num in enumerate(row):
                if idx == 0:
                    temp_row[0] = row_sum[0] + num
                elif idx == len(row)-1:
                    temp_row[level] = row_sum[level-1] + num
                else:
                    temp_row[idx] = min(row_sum[idx-1:idx+1]) + num
            row_sum = temp_row
        # return min(row_sum)
        return min(row_sum)



if __name__ == '__main__':
    triangle = [
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]
    ]
    print Solution().minimumTotal(triangle)
