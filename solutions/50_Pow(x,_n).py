# 50. Pow(x, n)
# Difficulty: Medium
# Contributor: LeetCode
# Implement pow(x, n).


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        elif n < 0:
            return 1 / self.myPow(x, -1 * n)
        elif n % 2:
            return x * self.myPow(x * x, n / 2)
        else:
            return self.myPow(x * x, n / 2)


if __name__ == '__main__':
    print Solution().myPow(2, 10)
    print Solution().myPow(2, 9)
    print Solution().myPow(2, -10)
