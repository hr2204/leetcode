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
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        for i in nums:
            if target - i in nums and i != target/2:
                res.append(nums.index(i))
                res.append( nums.index(target - i))
                break
        return res


s = Solution()
print s.twoSum([3,2,4], 6)
