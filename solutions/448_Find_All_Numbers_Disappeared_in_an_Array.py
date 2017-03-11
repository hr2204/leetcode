# -*- coding: utf-8 -*-
# 448. Find All Numbers Disappeared in an Array
# Difficulty: Easy
# Contributors: yuhaowang001
# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.
#
# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
#
# Example:
#
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [5,6]

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [i for i in xrange(1,len(nums)+1)]
        res = set(res)
        for num in nums:
            if num in res:
                res.remove(num)
        return list(res)
if __name__ == '__main__':
    input = [4,3,2,7,8,2,3,1]
    print Solution().findDisappearedNumbers(input)