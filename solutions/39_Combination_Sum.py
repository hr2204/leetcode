# 39. Combination Sum
# Difficulty: Medium
# Contributors: Admin
# Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
#
# The same repeated number may be chosen from C unlimited number of times.
#
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [2, 3, 6, 7] and target 7,
# A solution set is:
# [
#   [7],
#   [2, 2, 3]
# ]

import copy
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        res = []

        self.dfs(candidates,target,res,[])

        return res

    def dfs(self,candidates,target,res,cur_list):
        if sum(cur_list) == target:
            res.append(copy.deepcopy(cur_list))
        if sum(cur_list)<target:
            for idx in range(len(candidates)):
                cur_list.append(candidates[idx])
                self.dfs(candidates[idx:],target,res,cur_list)
                cur_list.pop()


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    print Solution().combinationSum(candidates, target)