# 40. Combination Sum II
# Difficulty: Medium
# Contributors: Admin
# Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the
# candidate numbers sums to T.
#
# Each number in C may only be used once in the combination.
#
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
import copy
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(candidates,target,res,[])

        return res

    def dfs(self,candidates, target,res,cur_list):
        if sum(cur_list) == target:
            cur_list.sort()
            res.append(copy.deepcopy(cur_list))
        if sum(cur_list) < target:
            for idx in range(len(candidates)):
                cur_list.append(candidates[idx])
                self.dfs(candidates[idx+1:],target,res,cur_list)
                cur_list.pop()



if __name__ == '__main__':
    candidate = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print Solution().combinationSum2(candidate,target)