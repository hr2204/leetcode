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

        def search(candidates,sum,cur):
            if sum == target:
                temp = sorted(cur)
                if temp not in res:
                    res.append(temp)
                return
            if sum > target:
                return
            for i in xrange(len(candidates)):
                search(candidates[i+1:],sum + candidates[i],cur+[candidates[i]])
        search(candidates,0,[])
        return res




if __name__ == '__main__':
    candidate = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print Solution().combinationSum2(candidate,target)