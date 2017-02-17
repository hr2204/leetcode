# -*- coding: utf-8 -*-
# 441. Arranging Coins
# Total Accepted: 16699
# Total Submissions: 46504
# Difficulty: Easy
# Contributors: Admin
# You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.
#
# Given n, find the total number of full staircase rows that can be formed.
#
# n is a non-negative integer and fits within the range of a 32-bit signed integer.
#
# Example 1:
#
# n = 5
#
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤
#
# Because the 3rd row is incomplete, we return 2.
# Example 2:
#
# n = 8
#
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤
#
# Because the 4th row is incomplete, we return 3.


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        while (start+1) * start<=2*n:
            start+=1
        return start - 1

if __name__ == '__main__':
    print Solution().arrangeCoins(8)