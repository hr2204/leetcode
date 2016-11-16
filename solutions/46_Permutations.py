# 46. Permutations
# Difficulty: Medium
# Contributors: Admin
# Given a collection of distinct numbers, return all possible permutations.
#
# For example,
# [1,2,3] have the following permutations:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<=1:
            return [nums]
        res = []

        for idx,num in enumerate(nums):
            for elem in self.permute(nums[:idx]+nums[idx+1:]):
                res.append([num]+ elem)

        return res



if __name__ == '__main__':
    nums = [1,2,3]
    print Solution().permute(nums)