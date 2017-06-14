# 96. Unique Binary Search Trees
# Difficulty: Medium
# Contributor: LeetCode
# Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
#
# For example,
# Given n = 3, there are a total of 5 unique BST's.
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[3] = dp[0] * dp[2] + dp[1] * dp[1] + dp[2] * dp[0]
        # dp[n] = dp[0] * dp[n-1] + dp[1] * dp[n-1] + .... + dp[n-1] * dp[1] + dp[n-1] * dp[0]
        dp = [1] * (n + 1)
        for i in xrange(2,n+1):
            dp_sum = 0
            for j in xrange(i):
                dp_sum += dp[j] * dp[i-1-j]
            dp[i] = dp_sum

        return dp[n]


if __name__ == '__main__':
    print Solution().numTrees(3)
