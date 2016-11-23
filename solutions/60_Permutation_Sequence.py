# -*- coding: utf-8 -*-
# 60. Permutation Sequence
# Difficulty: Medium
# Contributors: Admin
# The set [1,2,3,…,n] contains a total of n! unique permutations.
#
# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3):
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.
import math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        res = ""
        num_of_seq = math.factorial(n)
        num_list = range(1,n+1)
        for i in range(n)[::-1]:
            num_of_seq /= (i+1)
            num = 1
            while k > num_of_seq * num:
                num += 1
            res += str(num_list.pop(num-1))
            k -= num_of_seq * (num-1)

        return res






if __name__ == '__main__':
    print Solution().getPermutation(3,6) #213