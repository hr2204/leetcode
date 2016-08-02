# 283. Move Zeroes
# Difficulty: Easy
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
#
# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if 0 in nums:
            for i in range(len(nums)):
                firstZeroLoction = nums.index(0)
                if nums[i] != 0 and i >firstZeroLoction:
                    nums[i], nums[firstZeroLoction] = nums[firstZeroLoction], nums[i]


    def findFirstZero(self,nums):
        return nums.index(0)
    # solution 2
    def moveZeroes(self, nums):
        zero, cur = -1, 0
        while cur < len(nums):
            if nums[cur] != 0:
                # update zero index when current is not zero
                zero += 1
                nums[cur], nums[zero] = nums[zero], nums[cur]
            cur += 1

s = Solution()
nums = [1]
s.moveZeroes(nums)
# print s.findFirstZero(nums)
print nums
