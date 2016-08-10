# 371. Sum of Two Integers
# Difficulty: Easy
# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
#
# Example:
# Given a = 1 and b = 2, return 3.
#


class Solution(object):
    # Accepted
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX_INT = 0x7FFFFFFF
        MIN_INT = 0x80000000
        MASK = 0x100000000
        while b:
            a, b = (a ^ b) % MASK, ((a & b) << 1) % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)
    # Error: Time Limit Exceeded
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b:
            a = a ^ b
            carry = (a & b) << 1
            b = carry
        return a

    # Error: RuntimeError: maximum recursion depth exceeded in cmp
    def getSum_1(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if a == 0:
            return b
        digit = a ^ b
        carry = (a&b)<<1
        return self.getSum(carry,digit)

if __name__ == "__main__":
    assert Solution().getSum(1,-1) == 0
