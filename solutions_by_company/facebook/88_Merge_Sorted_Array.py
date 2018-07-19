# 88. Merge Sorted Array
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# Note:
#
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
# Example:
#
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# Output: [1,2,2,3,5,6]

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:] = nums2[:]

        nums1End = m - 1
        nums2End = n - 1
        last = m + n - 1
        while nums1End >= 0 and nums2End >= 0:
            print nums1End, last, nums2End
            if nums1[nums1End] >= nums2[nums2End]:
                nums1[last] = nums1[nums1End]
                nums1End -= 1
            else:
                nums1[last] = nums2[nums2End]
                nums2End -= 1
            last -= 1

        while nums2End >= 0:
            nums1[nums2End] = nums2[nums2End]
            nums2End -= 1

