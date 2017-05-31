# 560. Subarray Sum Equals K
# Difficulty: Medium
# Contributors:
# love_Fawn
# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
#
# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2
# Note:
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum = 0
        num_map = dict()
        num_map[0] = 1
        count = 0
        for num in nums:
            sum += num
            if sum - k in num_map:
                count += num_map[sum-k]
            if sum in num_map:
                num_map[sum] += 1
            else:
                num_map[sum] = 1

        return count



    def subarraySum_LTE(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        for i in xrange(len(nums)):
            sum = 0
            for j in xrange(i,len(nums)):
                sum += nums[j]
                if sum == k:
                    count += 1
        return count



if __name__ == '__main__':
    print Solution().subarraySum([1,1,1],2)
    print Solution().subarraySum([0, 4, 8, 3, 5, 2, 6, 7, 9, 1],12)