# 20. Valid Parentheses
# Difficulty: Easy
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s or len(s) % 2 != 0:
            return False

        stack = []
        left_parenthese = ['[','(','{']
        parentheses_map = {
            ']': '[',
            ')': '(',
            '}': '{'
        }

        for char in s:
            if char in left_parenthese:
                stack.append(char)
            else:
                if not stack or stack.pop() != parentheses_map[char]:
                    return False

        return not stack

if __name__ == '__main__':
    print Solution().isValid('((')