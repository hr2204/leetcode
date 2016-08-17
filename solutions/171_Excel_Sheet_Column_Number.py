# 171. Excel Sheet Column Number
# Difficulty: Easy
# Related to question Excel Sheet Column Title
#
# Given a column title as appear in an Excel sheet, return its corresponding column number.
#
# For example:
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        sList = list(s)
        res, i = 0, 0
        while sList:
            digit = sList[len(sList)-1]
            res += (ord(digit) - 64) * pow(26,i)
            i += 1
            sList.pop()
        return res
if __name__ == '__main__':
    print Solution().titleToNumber("ABC")