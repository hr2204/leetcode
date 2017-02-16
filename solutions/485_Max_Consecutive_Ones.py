# 485. Max Consecutive Ones
# Difficulty: Easy
# Contributors: Stomach_ache
# Given a binary array, find the maximum number of consecutive 1s in this array.
#
# Example 1:
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.
# Note:
#
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 1 not in nums:
            return 0
        if 0 not in nums:
            return len(nums)
        maxCon = nums.index(0)
        last_zero = maxCon
        for i in range(nums.index(0)+1,len(nums)):
            if nums[i] == 0:
                if i - last_zero >maxCon:
                    maxCon = i - last_zero - 1
                last_zero = i
        if nums[-1] == 1 and len(nums) - last_zero > maxCon:
            maxCon = len(nums) - last_zero -1

        return maxCon
if __name__ == '__main__':
    input = [0,1]
    print Solution().findMaxConsecutiveOnes(input)