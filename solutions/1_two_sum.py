# 1. Two Sum
# Difficulty: Easy
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# UPDATE (2016/2/13):
# The return format had been changed to zero-based indices. Please read the above updated description carefully.

class Solution(object):

    # o(n) solution
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        hash = {}
        for i in range(len(nums)):
            if target - nums[i] in hash:
                return [hash[target - nums[i]],i]
            hash[nums[i]] = i
        return [-1,1]

    # o(n^2) solution
    def twoSum_0(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        for i, num in enumerate(nums):
            if target - num in nums[i+1:]:
                res.append(i)
                res.append(nums[i+1:].index(target - num)+i+1)
        return res


s = Solution()
print s.twoSum([3,2,4],6)
