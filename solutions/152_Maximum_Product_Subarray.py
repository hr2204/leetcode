# 152. Maximum Product Subarray
# Difficulty: Medium
# Find the contiguous subarray within an array (containing at least one number) which has the largest product.
#
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.
#

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos_max = 0
        neg_max = 0

        for idx,num in enumerate(nums):
            if num > 0:
                pos_max * num
            if num = 0:

            if num < 0:
                neg_max * num
if __name__ == '__main__':
    nums = [2,3,-2,4]
    print Solution().maxProduct(nums)