# 136. Single Number
# Difficulty: Medium
# Given an array of integers, every element appears twice except for one. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numDict = dict()
        for num in nums:
            if num not in numDict:
                numDict[num] = 1
            else:
                numDict[num] += 1
        for num in numDict:
            if numDict[num]==1:
                return num

if __name__ == '__main__':
    assert Solution().singleNumber([1,1,2,2,3])