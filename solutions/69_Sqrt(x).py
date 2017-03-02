# 69. Sqrt(x)
# Difficulty: Easy
# Contributors: Admin
# Implement int sqrt(int x).
#
# Compute and return the square root of x.
#
# Subscribe to see which companies asked this question.

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        right = x/2 + 1
        left = 0
        mid = 0
        while left + 1 < right:
            mid = (left + right) /2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right = mid
            else:
                left = mid

        if right * right <= x:
            return right
        elif mid * mid <= x:
            return mid
        else:
            return left

if __name__ == '__main__':
    print Solution().mySqrt(1)