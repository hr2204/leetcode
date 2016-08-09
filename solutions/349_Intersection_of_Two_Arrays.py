# 349. Intersection of Two Arrays
# Difficulty: Easy
# Given two arrays, write a function to compute their intersection.
#
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
#
# Note:
# Each element in the result must be unique.
# The result can be in any order.


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        numDict = dict()
        res = []
        for num in nums1:
            if num not in numDict:
                numDict[num] = 1
        print numDict
        for num in nums2:
            if num in numDict and numDict[num] == 1:
                res.append(num)
                numDict[num] -= 1
        return res

if __name__ == "__main__":
    # assert Solution().rotate([1,2,3,4,5,6,7])
    Solution().intersection([1, 2, 2, 1], [2]) == [2]