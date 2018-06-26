# 279. Perfect Squares
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
#
# Example 1:
#
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
# Example 2:
#
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.

class Solution(object):
    def LTE_numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [n] * (n + 1)

        for i in range(n):
            if i * i <= n:
                dp[i * i] = 1

        for i in range(1, n + 1):
            for j in range(i):
                if i + j * j <= n:
                    dp[i + j * j] = min(dp[i + j * j], dp[i] + 1)

        return dp[n]


    _num = [0]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = self._num
        while len(num) <= n:
            num += min(num[-i * i] for i in xrange(1, int(len(num) ** 0.5 + 1))) + 1,
        return num[n]

if __name__ == '__main__':
    print Solution().numSquares(123)