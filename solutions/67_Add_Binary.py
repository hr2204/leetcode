# 67. Add Binary
# Difficulty: Easy
# Given two binary strings, return their sum (also a binary string).
#
# For example,
# a = "11"
# b = "1"
# Return "100".

class Solution(object):
    def addBinary(self, a, b):
        i, m, n, result, carry = 1, len(a), len(b), [], 0
        while i <= m or i <= n:
            temp = carry
            if i <= m:
                temp += int(a[-i])
            if i <= n:
                temp += int(b[-i])

            carry = temp / 2
            result.append(str(temp % 2))
            i += 1

        if carry:
            result.append(str(carry))

        return ''.join(result[::-1])


    def addBinary(self, a, b):
        return '{0:b}'.format(int(a, 2) + int(b, 2))

    def addBinary(self, a, b):
        return bin(int(a,2) + int(b,2))[2:]


    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a == "":
            return b
        if b == "":
            return a

        n = min(len(a), len(b))
        res = ""
        i = 1
        carry = 0
        while n > 0:
            digitA = int(a[-i])
            digitB = int(b[-i])
            res += str((carry + digitA + digitB) % 2)
            carry = (carry + digitA + digitB) / 2
            i += 1
            n -= 1
        # if len(a) == len(b):
        #     res += str(carry)

        while i <= len(a):
            digitA = int(a[-i])
            res += str((carry + digitA) % 2)
            carry = (carry + digitA) / 2
            i += 1
        while i <= len(b):
            digitB = int(b[-i])
            res += str((carry + digitB) % 2)
            carry = (carry + digitB) / 2
            i += 1
        if carry:
            res += str(carry)
        return res[::-1]


if __name__ == '__main__':
    print Solution().addBinary("10", "111")
