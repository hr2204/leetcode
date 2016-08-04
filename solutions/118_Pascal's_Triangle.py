# 118. Pascal's Triangle
# Difficulty: Easy
# Given numRows, generate the first numRows of Pascal's triangle.
#
# For example, given numRows = 5,
# Return
#
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        res = []
        if numRows <= 0:
            return res
        res = [[] for i in range(0, numRows)]
        res[0] = [1]
        if numRows == 1:
            return res
        res[1] = [1,1]
        if numRows == 2:
            return res
        for row in range(2, numRows):
            res[row].append(1)
            for col in range(1,row):
                res[row].append(res[row-1][col-1] + res[row-1][col])
            res[row].append(1)

        return res


s = Solution()
test = s.generate(5)
for x in test:
    print x
