# 300. Longest Increasing Subsequence
# Difficulty: Medium
# Contributors: Admin
# Given an unsorted array of integers, find the length of longest increasing subsequence.
#
# For example,
# Given [10, 9, 2, 5, 3, 7, 101, 18],
# The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.
#
# Your algorithm should run in O(n2) complexity.
#
# Follow up: Could you improve it to O(n log n) time complexity?
#

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        dp = [1]* len(nums)
        for cur,cur_num in  enumerate(nums):
            for pre,pre_num in enumerate(nums[:cur]):
                if cur_num > pre_num:
                    dp[cur] = max(dp[cur],dp[pre]+1)
        print dp
        return max(dp)


if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print Solution().lengthOfLIS(nums)