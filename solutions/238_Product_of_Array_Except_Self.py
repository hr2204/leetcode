# 238. Product of Array Except Self
# Difficulty: Medium
# Contributors: Admin
# Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all
# the elements of nums except nums[i].
#
# Solve it without division and in O(n).
#
# For example, given [1,2,3,4], return [24,12,8,6].
#
# Follow up:
# Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of
# space complexity analysis.)
#


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_len = len(nums)
        product_left = [1] * num_len
        product_right = [1] * num_len
        res = []
        for i in range(1,num_len):
            product_left[i] = product_left[i-1]*nums[i-1]
        for i in range(num_len-2,-1,-1):
            product_right[i] = product_right[i+1] * nums[i+1]
        for i in range(num_len):
            res.append(product_left[i]*product_right[i])
        return res





if __name__ == '__main__':
    print Solution().productExceptSelf([1,2,3,4])