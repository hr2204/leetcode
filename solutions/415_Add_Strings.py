# 415. Add Strings
# Total Accepted: 23323
# Total Submissions: 56606
# Difficulty: Easy
# Contributors: Admin
# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
#
# Note:
#
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        num1_len = len(num1)
        num2_len = len(num2)
        if num1_len > num2_len:
            num2 = (num1_len - num2_len) * '0' + num2

        if num1_len < num2_len:
            num1 = (num2_len - num1_len) * '0' + num1

        carry = 0
        res = ""
        idx = len(num1) - 1
        while idx > -1:
            digit_sum = int(num1[idx]) + int(num2[idx])
            res += str((digit_sum + carry)%10)
            if digit_sum + carry > 9:
                carry = 1
            else:
                carry = 0
            idx -= 1
        if carry:
            res += str(carry)
        return res[::-1]


if __name__ == '__main__':
    print Solution().addStrings('123', '987')
