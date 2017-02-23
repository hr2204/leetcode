# 279. Perfect Squares Add to List
# Difficulty: Medium
# Contributors: Admin
# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
#
# For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

import math
class Solution(object):

    _dp = [0]
    def numSquares(self, n):
        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]


    def numSquares_LTE(self,num):
        maxSquare = int(math.floor(math.sqrt(num)))
        if maxSquare == 1:
            return num

        if num == maxSquare * maxSquare:
            return 1

        tmp = 1 + self.helper(num - maxSquare * maxSquare)
        maxSquare -= 1
        while maxSquare > 0:
            cur = 1 + self.helper(num - maxSquare * maxSquare)
            if tmp > cur:
                tmp = cur

            maxSquare -= 1

        return tmp


if __name__ == '__main__':
    print Solution().numSquares(59)