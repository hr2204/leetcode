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
        if len(s) == 0 or len(s) == 1 or len(s)%2 == 1:
            return False
        list_1 = list()
        for i in s:
            if i == "(" or i == "[" or i == "{":
                list_1.append(i)
            if i == ")":
                if len(list_1) == 0 or list_1.pop()!="(":
                    return False
            if i == "]":
                if len(list_1) == 0 or list_1.pop()!="[":
                    return False
            if i == "}":
                if len(list_1) == 0 or list_1.pop()!="{":
                    return False

        return len(list_1) == 0
if __name__ == '__main__':
    print Solution().isValid("[")
    print Solution().isValid("{[]}")