# 22. Generate Parentheses
# Difficulty: Medium
# Contributors: Admin
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

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        if n < 1:
            return res
        self.helper(n, n, "", res)
        return res

    def helper(self, left, right, item, res):
        if right < left:
            return
        if left == 0 and right == 0:
            res.append(item)
        if left > 0:
            self.helper(left - 1, right, item + "(", res)
        if right > 0:
            self.helper(left, right - 1, item + ")", res)




            # def generateParenthesis(self, n):
            #     """
            #     :type n: int
            #     :rtype: List[str]
            #     """
            #     count = 1
            #     res = []
            #     res.append('()')
            #     while count<n:
            #         temp = res
            #         new = []
            #         for par in temp:
            #             left = "()" + par
            #             if left not in new:
            #                 new.append(left)
            #             right = par + "()"
            #             if right not in new:
            #                 new.append(right)
            #             round = "(" + par + ")"
            #             if round not in new:
            #                 new.append(round)
            #         res = new
            #         count += 1
            #     return res


if __name__ == '__main__':
    print Solution().generateParenthesis(3)
    # print "()()" in ['()()', '()()', '(())']
    # a = ["()()()()","(()()())","()(()())","(()())()","((()()))","()()(())","()(())()","(()(()))","(())()()","((())())","()((()))","((()))()","(((())))"]
    # b = ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
    # a.sort()
    # b.sort()
    # print a
    # print b
