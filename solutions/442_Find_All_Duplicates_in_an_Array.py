# -*- coding: utf-8 -*-
# 442. Find All Duplicates in an Array
# Difficulty: Medium
# Contributors: shen5630
# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements that appear twice in this array.
#
# Could you do it without extra space and in O(n) runtime?
#
# Example:
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [2,3]

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for num in nums:
            if nums[abs(num)-1]<0:
                res.append(abs(num))
            else:
                nums[abs(num)-1] *= -1
        return res

    def findDuplicates_extra_space(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        helper = [2]* len(nums)
        for num in nums:
            helper[num-1]-= 1

        res = []
        for i in range(len(helper)):
            if helper[i] == 0:
                res.append(i+1)
        return res

    def findDuplicates_LTE(self, nums):
        res = []
        for idx,num in enumerate(nums):
            if num in nums[:idx] and num not in res:
                res.append(num)
        return res

if __name__ == '__main__':
    input = [10,2,5,10,9,1,1,4,3,7]
    print Solution().findDuplicates(input)