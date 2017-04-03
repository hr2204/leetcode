# 53. Maximum Subarray
# Difficulty: Medium
# Contributors: Admin
# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.
#
# click to show more practice.
#
# More practice:
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = float('-inf')
        curSum = 0
        for num in nums:
            curSum = max(curSum + num,num)
            maxSum = max(maxSum,curSum)
        return maxSum



    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums, l, r):
        if l > r:
            return -2147483648

        m = l + (r - l) / 2
        left = self.helper(nums, l, m - 1)
        right = self.helper(nums, m + 1, r)

        leftMax = a = 0
        for i in range(m - 1, l - 1, -1):
            a += nums[i]
            leftMax = max(leftMax, a)

        rightMax = b = 0
        for i in range(m + 1, r + 1):
            b += nums[i]
            rightMax = max(rightMax, b)

        return max(leftMax + nums[m] + rightMax, max(left, right))

if __name__ == '__main__':
    nums =  [-2,1,-3,4,-1,2,1,-5,4]
    print Solution().maxSubArray(nums)