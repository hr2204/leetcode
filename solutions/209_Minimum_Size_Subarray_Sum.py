# -*- coding: utf-8 -*-
# 209. Minimum Size Subarray Sum
# Difficulty: Medium
# Contributors: Admin
# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s.
# If there isn't one, return 0 instead.
#
# For example, given the array [2,3,1,2,4,3] and s = 7,
# the subarray [4,3] has the minimal length under the problem constraint.
#
# click to show more practice.
#
# More practice:
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

class Solution(object):
    def minSubArrayLen(self, s, nums):
        size = len(nums)
        start, end, sum = 0, 0, 0
        bestAns = size + 1
        while True:
            if sum < s:
                if end >= size:
                    break
                sum += nums[end]
                end += 1
            else:
                if start > end:
                    break
                bestAns = min(end - start, bestAns)
                sum -= nums[start]
                start += 1
        return [0, bestAns][bestAns <= size]


    def minSubArrayLen_LTE(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        min_res = len(nums)
        if sum(nums)<s:
            return 0
        for i in range(len(nums)):
            if nums[i] >= s:
                return 1
            sums = nums[i]
            count = 1
            for j in range(i+1,len(nums)):
                sums += nums[j]
                count += 1
                if sums >= s:
                    min_res = min(min_res,count)
                    break

        return min_res

if __name__ == '__main__':
    list = [2,3,1,2,4,3]
    target = 7
    print Solution().minSubArrayLen(target,list)