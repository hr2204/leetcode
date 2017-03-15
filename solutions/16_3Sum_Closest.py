# 16. 3Sum Closest
# Difficulty: Medium
# Contributors: Admin
# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
# Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
#     For example, given array S = {-1 2 1 -4}, and target = 1.
#
#     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()
        res = None
        for i in xrange(len(nums)):
            left,right = i + 1, len(nums)-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if res is None or abs(target - sum) < abs(target - res):
                    res = sum
                if sum <= target:
                    left += 1
                else:
                    right -= 1
        return res



    def threeSumClosest_LTE(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = nums[0] + nums[1] + nums[2]
        diff = abs(target - res)
        for i in xrange(len(nums)-2):
            two_closet = self.twoSumCloset(nums[i+1:],target-nums[i])
            print two_closet, nums[i]
            if abs(target - (two_closet + nums[i])) < diff:
                res = two_closet + nums[i]
                diff = abs(target - (two_closet + nums[i]))
        return res

    def twoSumCloset(self,nums,target):
        res = nums[0] + nums[1]
        diff = abs(target - res)
        for i in xrange(len(nums)-1):
            for j in xrange(i+1,len(nums)):
                cur_two_sum = nums[i] + nums[j]
                if abs(target - cur_two_sum) < diff:
                    res = cur_two_sum
                    diff = abs(target - cur_two_sum)
        return res

if __name__ == '__main__':
    a = [0,1,2]
    b = 0
    print Solution().threeSumClosest(a,b)