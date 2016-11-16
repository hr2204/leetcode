#coding:utf-8
# 215. Kth Largest Element in an Array
# Difficulty: Medium
# Contributors: Admin
# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# For example,
# Given [3,2,1,5,6,4] and k = 2, return 5.
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == len(nums):
            return min(nums)
        k_list = []
        for num in nums:
            if len(k_list)<k:
                k_list.append(num)
            else:
                k_list.append(num)
                k_list.sort(reverse=True)
                k_list.pop()

        return k_list[-1]

if __name__ == '__main__':
    nums = [3,2,1,5,6,4]
    k = 2
    print Solution().findKthLargest(nums,k)
    print Solution().findKthLargest([-1,-2,0],3)