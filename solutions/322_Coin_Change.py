# 322. Coin Change
# Total Accepted: 50832
# Total Submissions: 194735
# Difficulty: Medium
# Contributors: Admin
# You are given coins of different denominations and a total amount of money amount. Write a function to compute the
# fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any
# combination of the coins, return -1.
#
# Example 1:
# coins = [1, 2, 5], amount = 11
# return 3 (11 = 5 + 5 + 1)
#
# Example 2:
# coins = [2], amount = 3
# return -1.
#
# Note:
# You may assume that you have an infinite number of each kind of coin.
import math
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float("inf")]* (amount+1)
        dp[0] = 0

        for i in range(1,amount+1):
            for coin in coins:
                if i - coin >=0 and dp[i-coin] != float("inf") and dp[i-coin] + 1< dp[i]:
                    dp[i] = dp[i-coin] + 1
        return dp[-1] if dp[-1]!= float("inf") else -1


if __name__ == '__main__':
    coins = [1,2,5]
    amount = 11
    print Solution().coinChange(coins,amount)