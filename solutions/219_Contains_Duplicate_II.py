# 219. Contains Duplicate II
# Difficulty: Easy
# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in
# the array such that nums[i] = nums[j] and the difference between i and j is at most k.

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        numDict = dict()
        for i in range(len(nums)):
            idx = numDict.get(nums[i])
            if idx>=0 and i - idx <=k:
                return True
            numDict[nums[i]] = i
        return False
    # Solution 1: too slow
    # def containsNearbyDuplicate(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: bool
    #     """
    #     if len(nums) == 0 or len(nums) == 1: return False
    #     if k>=len(nums):
    #         return self.containsDuplicate(nums)
    #     else:
    #         for i in range(0,len(nums)-k+1):
    #            if self.containsDuplicate(nums[i:i+k+1]):
    #                 return True
    #     return False
    #
    #
    #
    # def containsDuplicate(self,nums):
    #     return len(nums)!=len(set(nums))


s = Solution()
print s.containsNearbyDuplicate([2,1,2],1)


        # wrong
        # numSet = set()
        # for i, num in enumerate(nums):
        #     if num in numSet and i - nums.index(num) <= k:
        #         return True
        #     numSet.add(num)
        # return False


        # Input:
        # [1,0,1,1]
        # 1
        # Output:
        # false
        # Expected:
        # true