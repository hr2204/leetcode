# 4. Median of Two Sorted Arrays
# Difficulty: Hard
# Contributor: LeetCode
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# Example 1:
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged_list = []
        idx1, idx2 = 0, 0
        res = 0

        while idx1 < len(nums1) and idx2 < len(nums2):
            if nums1[idx1] <= nums2[idx2]:
                merged_list.append(nums1[idx1])
                idx1 += 1
            else:
                merged_list.append(nums2[idx2])
                idx2 += 1

        if idx1 < len(nums1):
            merged_list += nums1[idx1:]
        if idx2 < len(nums2):
            merged_list += nums2[idx2:]

        if len(merged_list)%2 == 0:
            res = (merged_list[len(merged_list)/2] + merged_list[len(merged_list)/2-1])/2.0
        else:
            res = merged_list[len(merged_list)/2]

        return res



if __name__ == '__main__':
    print Solution().findMedianSortedArrays([1,3],[2])
    print Solution().findMedianSortedArrays([1,2],[3,4])