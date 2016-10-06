# 268. Missing Number
# Difficulty: Medium
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#
# For example,
# Given nums = [0, 1, 3] return 2.
#
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
#
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        end = len(nums)
        target_sum = (len(nums) + 1) * (0 + end) / 2

        return target_sum - sum(nums)


if __name__ == '__main__':
    print Solution().missingNumber([0, 2]) == 1
    print Solution().missingNumber([1]) == 0
    print Solution().missingNumber([0, 1, 2]) == 3

