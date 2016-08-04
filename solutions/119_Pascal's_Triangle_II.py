# 119. Pascal's Triangle II
# Difficulty: Easy
# Given an index k, return the kth row of the Pascal's triangle.
#
# For example, given k = 3,
# Return [1,3,3,1].

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = []
        if rowIndex<0:
            return res
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        preRow = self.getRow(rowIndex-1)
        res.append(1)
        for idx in range(1,rowIndex):
            res.append(preRow[idx] + preRow[idx-1])
        res.append(1)
        return res

s = Solution()

print s.getRow(4)