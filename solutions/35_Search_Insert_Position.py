#-*-coding:utf-8 -*-
# 35. Search Insert Position
# Difficulty: Medium
# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if
# it were inserted in order.
#
# You may assume no duplicates in the array.
#
# Here are few examples.
# [1,3,5,6], 5 → 2
# [1,3,5,6], 2 → 1
# [1,3,5,6], 7 → 4
# [1,3,5,6], 0 → 0

class Solution(object):
    def searchInsert_jiuzhang(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        start, end = 0, len(nums) - 1
        # first position >= target
        while start + 1 < end:
            mid = (start + end) / 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid

        if nums[start] >= target:
            return start
        if nums[end] >= target:
            return end
        return len(nums)


    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        if target<nums[0]:
            return 0
        if target>nums[end]:
            return end + 1
        while start <= end:
            mid = start + (end - start)/2
            if nums[mid]<target<=nums[mid+1]:
                return mid + 1
            if nums[mid] == target:
                return mid
            if nums[mid]>target:
                end = mid
            if nums[mid]<target:
                start = mid


if __name__ == '__main__':
    print Solution().searchInsert([1,3],3) == 1
    print Solution().searchInsert([1],1) == 0
    print Solution().searchInsert([1,3,5,6],5) == 2
    print Solution().searchInsert([1,3,5,6],2) == 1
    print Solution().searchInsert([1,3,5,6],7) == 4
    print Solution().searchInsert([1,3,5,6],0) == 0