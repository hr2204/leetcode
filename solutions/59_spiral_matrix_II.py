# 59. Spiral Matrix II
# Difficulty: Medium
# Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
#
# For example,
# Given n = 3,
#
# You should return the following matrix:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]
class Solution:
    def generateMatrix(self,n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 0:
            return []
        res = []
        # generate 2d array
        res = [[0 for i in range(n)] for j in range(n)]

        # for i in range(0,n):
        #     temp = []
        #     for j in range(0,n):
        #         temp.append(0)
        #     res.append(temp)
        left = 0
        right = n - 1
        top = 0
        bot = n - 1
        num = 1
        while left<=right and top<=bot:
            for i in range(left,right+1):
                res[top][i]= num
                num +=1
            top +=1
            for i in range(top,bot+1):
                res[i][right] = num
                num +=1
            right -=1
            for i in range(left,right+1)[::-1]:
                res[bot][i] = num
                num +=1
            bot -=1
            for i in range(top,bot+1)[::-1]:
                res[i][left] = num
                num +=1
            left +=1
        return res


s = Solution()

print s.generateMatrix(2)