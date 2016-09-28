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
        res[0] = self.binary_search_left(nums,target)
        res[1] = self.binary_search_right(nums,target)
        return res

    def binary_search_left(self,nums,target):
        if not nums:
            return -1
        start,end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start)/2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                start = mid
            else:
                end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

    def binary_search_right(self,nums,target):
        if not nums:
            return -1
        start,end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start)/2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                start = mid
            else:
                end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1




if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    print Solution().binary_search(nums,8)
    # print Solution().searchRange(nums,8) == [3,4]