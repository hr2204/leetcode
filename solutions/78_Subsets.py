# 78. Subsets
# Difficulty: Medium
# Given a set of distinct integers, nums, return all possible subsets.
#
# Note: The solution set must not contain duplicate subsets.
#
# For example,
# If nums = [1,2,3], a solution is:
#
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

class Solution(object):
    def subsets2(self, S):
        def dfs(depth, start, valuelist):
            res.append(valuelist)
            if depth == len(S): return
            for i in range(start, len(S)):
                dfs(depth+1, i+1, valuelist+[S[i]])
        S.sort()
        res = []
        dfs(0, 0, [])
        return res


    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for idx in range(len(nums)):
            res += self.dfs(nums,idx)
        res.append(nums)
        return res

    def dfs(self,nums,num_elem):
        res = []
        if num_elem == 0:
            return [[]]
        if num_elem == 1:
            for idx in range(len(nums)):
                res.append([nums[idx]])
            return res
        if num_elem > 1:
            for idx in range(len(nums)):
                next_res = self.dfs(nums[idx+1:],num_elem-1)
                for i in range(len(next_res)):
                    res.append([nums[idx]]+next_res[i])
            return res

if __name__ == '__main__':
    print Solution().subsets2([1,2,3])