# 169. Majority Element
# Difficulty: Easy
# Given an array of size n, find the majority element. The majority element is the element that appears more than
# [ n/2 ] times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numDict = dict()
        for num in nums:
            if num in numDict:
                numDict[num] += 1
            else:
                numDict[num] = 1
            if numDict[num] > len(nums) / 2:
                return num

print Solution().majorityElement([1,1,2,2,3,3,3,3,3])

if __name__ == "__main__":
    assert Solution().majorityElement([1,1,2,2,3,3,3,3,3]) == 3