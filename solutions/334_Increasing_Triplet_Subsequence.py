# -*- coding: utf-8 -*-
# 334. Increasing Triplet Subsequence
# Difficulty: Medium
# Contributors: Admin
# Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.
#
# Formally the function should:
# Return true if there exists i, j, k
# such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
# Your algorithm should run in O(n) time complexity and O(1) space complexity.
#
# Examples:
# Given [1, 2, 3, 4, 5],
# return true.
#
# Given [5, 4, 3, 2, 1],
# return false.

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if not nums:
            return False

        flag = False
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                flag = True
        if not flag:
            return False

        dp = [1] * len(nums)
        for cur,cur_num in enumerate(nums):
            for pre,pre_num in enumerate(nums[:cur]):
                if cur_num > pre_num:
                    dp[cur] = max(dp[cur],dp[pre]+1)
                if dp[cur] == 3:
                    return True
        return False

if __name__ == '__main__':
    test_case_1 = [1, 2, 3, 4, 5]
    test_case_2 = [5, 4, 3, 2, 1]
    test_case_3 = [2,1,5,0,4,6]
    # print Solution().increasingTriplet(test_case_1)
    # print Solution().increasingTriplet(test_case_2)
    print Solution().increasingTriplet(test_case_3)