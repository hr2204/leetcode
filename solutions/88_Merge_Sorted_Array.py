# 88. Merge Sorted Array
# Difficulty: Easy
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# Note:
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
# The number of elements initialized in nums1 and nums2 are m and n respectively.


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        idx = m + n - 1
        idxM = m - 1
        idxN = n - 1
        while idxM>=0 and idxN >=0:
            if nums1[idxM] > nums1[idxN]:
                nums1[idx] = nums1[idxM]
                idxM -= 1
            else:
                nums1[idx] = nums1[idx]
                idxN -= 1
        if m < 0:
            nums1[:idx] = nums2[idxN]
        if n < 0:
            nums1[:idx] = nums1[:idxM]

    def merge_lazyVersion(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = nums1[:m]
        nums1[:] = nums1 + nums2
        nums1[:].sort()

if __name__ == "__main__":
    # assert Solution().rotate([1,2,3,4,5,6,7])
    Solution().merge([1], 1,[0],0)
