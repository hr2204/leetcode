# 34. Search for a Range
# Difficulty: Medium
# Given a sorted array of integers, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1,-1]
        if not nums:
            return res

        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = (start + end)/2
            if nums[mid]<target:
                start = mid
            else:
                end = mid

        if nums[start] == target:
            leftBound = start
        elif nums[end] == target:
            leftBound = end
        else:
            return [-1, -1]

        start = leftBound
        end = len(nums) - 1

        while start + 1 < end:
            mid = (start + end)/2
            if nums[mid]<=target:
                start = mid
            else:
                end = mid
        if nums[end] == target:
            rightBound = end
        else:
            rightBound = start

        return [leftBound,rightBound]


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    print Solution().searchRange(nums,8)
    # print Solution().searchRange(nums,8) == [3,4]