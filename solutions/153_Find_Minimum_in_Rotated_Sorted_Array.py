# 153. Find Minimum in Rotated Sorted Array
# Difficulty: Medium
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# Find the minimum element.
#
# You may assume no duplicate exists in the array.

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        nums_len = len(nums)
        start = 0
        end = nums_len - 1
        while start < end:
            mid = start + (end - start)/2
            if nums[mid]>nums[end]:
                start = mid + 1
            else:
                end = mid
        return nums[end]


    # def is_increasing(self,nums):
    #     res = True
    #     for i in range(1,len(nums)):
    #         if nums[i]< nums[i-1]:
    #             res = False
    #             break
    #     return res

if __name__ == '__main__':
    print Solution().findMin([1,2,3])
