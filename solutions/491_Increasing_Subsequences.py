# 491. Increasing Subsequences
#
# Difficulty: Medium
# Contributors: Stomach_ache
# Given an integer array, your task is to find all the different possible increasing subsequences of the given array,
# and the length of an increasing subsequence should be at least 2 .
#
# Example:
# Input: [4, 6, 7, 7]
# Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
# Note:
# The length of the given array will not exceed 15.
# The range of integer in the given array is [-100,100].
# The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.

class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dp = set()
        for n in nums:
            for y in list(dp):
                if n >= y[-1]:
                    dp.add(y + (n,))
            dp.add((n,))
        return list(e for e in dp if len(e) > 1)

    def findSubsequences_LTE(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return
        res = []
        self.res_map = {}
        for i in range(len(nums)):
            cur_list = [nums[i]]
            self.helper(cur_list,nums[i+1:],res)
        return res

    def helper(self,cur_list,nums,res):
        if not nums:
            return
        for idx,num in enumerate(nums):
            if num >= cur_list[-1]:
                temp = cur_list + [num]
                temp_key = ''.join(map(str, temp))
                if temp_key not in self.res_map:
                    res.append(temp)
                    self.res_map[temp_key] = 1
                    self.helper(temp,nums[idx+1:],res)



if __name__ == '__main__':
    input = [1,2,3,1,1]
    print Solution().findSubsequences(input)