# 168. Excel Sheet Column Title
# Difficulty: Easy
# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
#
# For example:
#
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ""
        while n:
            if n%26 == 0:
                res += str(unichr(90))
                n = n/26 - 1
            else:
                res += str(unichr((n%26) + 64))
                n = n/26

        return res[::-1]
if __name__ == '__main__':
    print Solution().convertToTitle(702)