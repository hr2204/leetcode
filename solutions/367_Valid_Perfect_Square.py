# 367. Valid Perfect Square
# Difficulty: Medium
# Given a positive integer num, write a function which returns True if num is a perfect square else False.
#
# Note: Do not use any built-in library function such as sqrt.
#
# Example 1:
#
# Input: 16
# Returns: True
# Example 2:
#
# Input: 14
# Returns: False

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        res = False
        i = 1
        while True:
            if i * i > num:
                return False
            if i * i == num:
                return True
            i += 1
        return res
if __name__ == '__main__':
    print Solution().isPerfectSquare(16)
    print Solution().isPerfectSquare(14)