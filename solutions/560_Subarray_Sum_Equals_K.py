# 560. Subarray Sum Equals K
# Difficulty: Medium
# Contributors:
# love_Fawn
# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
#
# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2
# Note:
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

from random import shuffle

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum = nums[0]
        left, right = 0, 0
        while True:
            while sum < k:
                right += 1
                sum += nums[right]

            while sum > k:
                sum -= nums[left]
                left += 1

            if sum == k:
                break

        return right - left + 1


if __name__ == '__main__':
    print Solution().subarraySum([1,1,1],2)
    print Solution().subarraySum([0, 4, 8, 3, 5, 2, 6, 7, 9, 1],12)