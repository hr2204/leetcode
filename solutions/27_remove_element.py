# 27. Remove Element
# Difficulty: Easy
# Given an array and a value, remove all instances of that value in place and return the new length.
#
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
#
# Example:
# Given input array nums = [3,2,2,3], val = 3
#
# Your function should return length = 2, with the first two elements of nums being 2.
#
# Hint:
#
# Try two pointers.
# Did you use the property of "the order of elements can be changed"?
# What happens when the elements to remove are rare?

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0: return 0
        if val not in nums: return len(nums)
        start = 0
        end = len(nums) - 1
        while start < end:
            if nums[start] == val and nums[end] == val:
                end -= 1
            elif nums[start] == val and nums[end] != val:
                nums[start], nums[end] = nums[end],nums[start]
            elif nums[start] != val and nums[end] == val:
                start += 1
            else:
                start += 1
        print nums
        return nums.index(val)
    # solution 1
    def removeElement1(self, A, elem):
        index = 0
        for num in A:
            if num != elem:
                A[index] = num
                index += 1
        print A
        return index


s = Solution()
print s.removeElement1([3, 2, 2, 3],2)
