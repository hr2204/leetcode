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
        pos_max, neg_max = [], []
        pos_max.append(nums[0])
        neg_max.append(nums[0])
        res = nums[0]
        for i in range(1,len(nums)):
            pos_max.append( max(pos_max[i-1]*nums[i],neg_max[i-1]*nums[i],nums[i]) )
            neg_max.append( min(pos_max[i-1]*nums[i],neg_max[i-1]*nums[i],nums[i]) )
            res = max(pos_max[i],res)
        return res

if __name__ == '__main__':
    nums = [2,3,-2,4]
    print Solution().maxProduct(nums)