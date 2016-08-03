# 217. Contains Duplicate
# Difficulty: Easy
# Given an array of integers, find if the array contains any duplicates. Your function should retur
# n true if any value appears at least twice in the array, and it should return false if every element is distinct.

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Solution 1: Time Limit Exceeded
        # if len(nums) == 0 or len(nums) == 1: return False
        # for i,num in enumerate(nums):
        #     if num in nums[i+1:]:
        #         return True
        #
        # return False

        # Solution 2: Correct
        # return len(nums)!= len(set(nums))


        # Solution 3: Correct
        numSet = set()
        for i in nums:
            if i in numSet:
                return True
            numSet.add(i)
        return False

s = Solution()
print s.containsDuplicate([1,2,3,1])