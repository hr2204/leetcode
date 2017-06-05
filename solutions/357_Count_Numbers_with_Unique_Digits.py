# -*- coding: utf-8 -*-
# 357. Count Numbers with Unique Digits
# Difficulty: Medium
# Contributor: LeetCode
# Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.
#
# Example:
# Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding
# [11,22,33,44,55,66,77,88,99])
#
# Credits:
# Special thanks to @memoryless for adding this problem and creating all test cases.

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0


        def dfs(str,count,n):
            if len(str) == n:
                return
            for i in '0123456789':
                if i not in str:
                    str += i
                    count += 1
                    dfs(str,count,n)
                    str = str[:-1]

        dfs("",count,n)
        return count
if __name__ == '__main__':
    print Solution().countNumbersWithUniqueDigits(1)