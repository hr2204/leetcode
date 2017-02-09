# 3. Search in Rotated Sorted Array
#
# Difficulty: Medium
# Contributors: Admin
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#
# Subscribe to see which companies asked this question.
#



class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        start=0
        end=len(nums)-1

        while start<=end:

            mid=(start+end)/2

            if nums[mid]==target:
                return mid

            if nums[mid]>=nums[start]:

                if target>=nums[start] and target<nums[mid]:
                    end=mid-1
                else:
                    start=mid+1

            if nums[mid]<nums[end]:

                if target>nums[mid] and target<=nums[end]:
                    start=mid+1
                else:
                    end=mid-1

        return -1


if __name__ == '__main__':
    input = [4, 5, 6, 7, 0, 1, 2]
    input = [1]
    target = 6
    print Solution().search(input,target)