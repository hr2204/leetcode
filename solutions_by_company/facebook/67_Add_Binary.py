# 67. Add Binary
#
# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Example 1:
#
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
#
# Input: a = "1010", b = "1011"
# Output: "10101"

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        end_a = len(a) - 1
        end_b = len(b) - 1
        carry = 0
        res = ""

        while end_a >= 0 and end_b >= 0:
            digit = (int(a[end_a]) + int(b[end_b]) + carry) % 2
            carry = (int(a[end_a]) + int(b[end_b]) + carry) / 2
            res = str(digit) + res
            end_a -= 1
            end_b -= 1

        if end_a >= 0:
            left = end_a
            temp = a
        else:
            left = end_b
            temp = b

        while left >= 0:
            digit = (int(temp[left]) + carry) % 2
            carry = (int(temp[left]) + carry) / 2
            left -= 1
            res = str(digit) + res

        if carry:
            res = str(carry) + res

        return res