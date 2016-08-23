# 70. Climbing Stairs
# Difficulty: Easy
# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        num_1 = 1
        num_2 = 2
        if n == 1:
            return num_1
        if n == 2:
            return num_2
        for i in range(3,n+1):
            res = num_1 + num_2
            num_1 = num_2
            num_2 = res
        return res

    # TLE
    def climbStairs_TLE(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


if __name__ == '__main__':
    n = 5
    print Solution().climbStairs(n)
    print Solution().climbStairs_TLE(n)