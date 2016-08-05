# 189. Rotate Array
# Difficulty: Easy
# Rotate an array of n elements to the right by k steps.
#
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
#
# Note:
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
#
# [show hint]
#
# Hint:
# Could you do it in-place with O(1) extra space?
# Related problem: Reverse Words in a String II
#


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        idx = len(nums) - k - 1
        print idx
        nums = nums[idx+1:] + nums[:idx+1]
        print nums

    def rotate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        k = k%len(nums)
        while k > 0:
            nums.insert(0,nums[-1])
            nums.pop()
            k -= 1

        print nums




if __name__ == "__main__":
    # assert Solution().rotate([1,2,3,4,5,6,7])
    Solution().rotate2([1,2,3],4)