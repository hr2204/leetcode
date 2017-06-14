# 89. Gray Code
# Difficulty: Medium
# Contributor: LeetCode
# The gray code is a binary numeral system where two successive values differ in only one bit.
#
# Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code.
# A gray code sequence must begin with 0.
#
# For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
#
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
# Note:
# For a given n, a gray code sequence is not uniquely defined.
#
# For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.
#
# For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.
#

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        return [int(data, 2) for data in self.dfs(n)]

    def dfs(self, n):
        if n == 1:
            return ['0', '1']

        code = self.dfs(n-1)
        part1 = ['0' + bin for bin in code]
        part2 = ['1' + bin for bin in code[::-1]]

        return part1 + part2

if __name__ == '__main__':
    print Solution().grayCode(3)


