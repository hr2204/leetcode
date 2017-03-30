# 416. Partition Equal Subset Sum
# Total Accepted: 15143
# Total Submissions: 39573
# Difficulty: Medium
# Contributors: Admin
# Given a non-empty array containing only positive integers, find if the array can be partitioned into
# two subsets such that the sum of elements in both subsets is equal.
#
# Note:
# Each of the array element will not exceed 100.
# The array size will not exceed 200.
# Example 1:
#
# Input: [1, 5, 11, 5]
#
# Output: true
#
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:
#
# Input: [1, 2, 3, 5]
#
# Output: false
#
# Explanation: The array cannot be partitioned into equal sum subsets.

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        mySum = sum(nums)
        if mySum % 2 == 1:
            return False
        mySum /= 2
        dp = [False for x in range(mySum+1)]
        dp[0] = True
        # for i in range(0,length):
        #     for j in range(mySum, nums[i] - 1, -1):
        #         dp[j] |= dp[j - nums[i]]

        for i in xrange(length):
            if nums[i]<= mySum:
                temp = [j for j in xrange(len(dp)) if dp[j]]
                for k in xrange(len(temp)):
                    if temp[k] + nums[i] <=mySum:
                        dp[temp[k] + nums[i]] = True
            print dp

                # for j in xrange(len(dp)):
                #     if dp[j] and j + nums[i] <= mySum:
                #         dp[j+nums[i]] = True
        return dp[mySum]


if __name__ == '__main__':
    print Solution().canPartition([2,2,3,5])
    print Solution().canPartition([5,4,7,1,5])