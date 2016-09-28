#-*-coding:utf-8 -*-
# 162. Find Peak Element
# Difficulty: Medium
# A peak element is an element that is greater than its neighbors.
#
# Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.
#
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
#
# You may imagine that num[-1] = num[n] = -∞.
#
# For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
#
# click to show spoilers.
#
# Note:
# Your solution should be in logarithmic complexity.


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        if len(nums) == 1:
            return nums[0]
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start)/2
            if nums[mid - 1]<nums[mid] and nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid - 1]<nums[mid] < nums[mid + 1]:
                start = mid
            else:
                end = mid
        if nums[start] > nums[start+1]:
            return start
        if nums[end] > nums[end-1]:
            return end
if __name__ == '__main__':
    print Solution().findPeakElement([1,2,3,1]) == 2