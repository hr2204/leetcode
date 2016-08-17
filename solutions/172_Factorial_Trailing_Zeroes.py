# 172. Factorial Trailing Zeroes
# Difficulty: Easy
# Given an integer n, return the number of trailing zeroes in n!.
#
# Note: Your solution should be in logarithmic time complexity.

class Solution(object):


    def trailingZeroes(self, n):

        res = 0
        while n > 0:
            tmp = n/5
            res += tmp
            n = tmp
        return res

    # Submission Result: Time Limit Exceeded
    # Last executed input: 1808548329
    def trailingZeroes_slow(self, n):
        """
        :type n: int
        :rtype: int
        """
        temp = 5
        res = 0
        while temp <= n:
            i = 1
            while i*temp <= n:
                res += 1
                i += 1
            temp *= 5
        return res

if __name__ == '__main__':
    print Solution().trailingZeroes(0)