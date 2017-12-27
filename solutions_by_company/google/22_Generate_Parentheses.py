# 22. Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        self.dfs(res, '', n, n)
        return res

    def dfs(self, res, str, left, right):
        if left > right:
            return

        if left == 0 and right == 0:
            print(str)
            res.append(str)
            return

        if left > 0:
            self.dfs(res, str + '(', left - 1, right)

        if right > 0:
            self.dfs(res, str + ')', left, right - 1)

if __name__ == '__main__':
    print(Solution().generateParenthesis(3))