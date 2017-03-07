# 47. Permutations II
# Difficulty: Medium
# Contributors: Admin
# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
#
# For example,
# [1,1,2] have the following unique permutations:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        hash_map = {}
        return self.helper(nums)

    def helper(self,nums):
        if len(nums) <= 1:
            return [nums]
        res = []

        hash_map = []
        for idx,num in enumerate(nums):
            if num not in hash_map:
                hash_map.append(num)
                # print hash_map
                for elem in self.helper(nums[:idx]+nums[idx+1:]):
                    res.append([num]+ elem)
            else:
                continue
        return res

    # LTE case: [3,3,0,0,2,3,2]
    def permuteUnique_LTE(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<=1:
            return [nums]
        res = []

        for idx,num in enumerate(nums):
            for elem in self.permuteUnique(nums[:idx]+nums[idx+1:]):
                temp = [num]+ elem
                if temp not in res:
                    res.append(temp)

        return res

if __name__ == '__main__':
    input = [1,1,2]
    print Solution().permuteUnique(input)