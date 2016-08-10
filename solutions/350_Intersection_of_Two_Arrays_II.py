# 350. Intersection of Two Arrays II
# Difficulty: Easy
# Given two arrays, write a function to compute their intersection.
#
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
#
# Note:
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.
# Follow up:
# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot
# load all elements into the memory at once?

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        numDict = dict()
        res = []
        for num in nums1:
            if num not in numDict:
                numDict[num] = [0,0]
                numDict[num][0] = 1
            else:
                numDict[num][0] += 1
        for num in nums2:
            if num not in numDict:
                numDict[num] = [0,0]
                numDict[num][1] = 1
            else:
                numDict[num][1] += 1
        print numDict
        for numKey in numDict:
            if numDict[numKey][0]< numDict[numKey][1]:
                res = res + [numKey]* numDict[numKey][0]
            else:
                res = res + [numKey]* numDict[numKey][1]
        return res

if __name__ == "__main__":
    # assert Solution().rotate([1,2,3,4,5,6,7])
    assert Solution().intersect([1], [1,1]) == [1]