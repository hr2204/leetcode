# 494. Target Sum
# Difficulty: Medium
# Contributors: kevin.xinzhao@gmail.com
# You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -.
# For each integer, you should choose one from + and - as its new symbol.
#
# Find out how many ways to assign symbols to make sum of integers equal to target S.
#
# Example 1:
# Input: nums is [1, 1, 1, 1, 1], S is 3.
# Output: 5
# Explanation:
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
#
# There are 5 ways to assign symbols to make the sum of nums be target 3.
# Note:
# The length of the given array is positive and will not exceed 20.
# The sum of elements in the given array will not exceed 1000.
# Your output answer is guaranteed to be fitted in a 32-bit integer.
import time, collections

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        dp = collections.Counter()
        dp[0] = 1
        for n in nums:
            ndp = collections.Counter()
            for sgn in (1, -1):
                for k in dp.keys():
                    ndp[k + n * sgn] += dp[k]
            dp = ndp
        return dp[S]


    def findTargetSumWays_LTE(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        nums = sorted(nums,reverse=True)
        input = []
        zero_count = 0
        for num in nums:
            if num != 0:
                input.append(num)
            else:
                zero_count += 1
        if zero_count == len(nums) and S == 0:
            return pow(2,zero_count)
        return self.dfs(input,S) * pow(2,zero_count)

    def dfs(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        temp = sum(nums)
        if temp < S or temp < -1 * S:
            return 0
        if len(nums) == 0:
            return 0
        if len(nums) == 1 and (nums[0] == S or nums[0] + S == 0):
            return 1

        return self.dfs(nums[1:],S - nums[0]) + self.dfs( nums[1:],S + nums[0])


if __name__ == '__main__':
    nums = [42,36,4,15,17,15,31,1,11,2,12,28,22,9,2,31,48,18,48,5]

    s = 15
    start = time.clock()
    print Solution().findTargetSumWays(nums,s)
    end = time.clock()
    print end-start
