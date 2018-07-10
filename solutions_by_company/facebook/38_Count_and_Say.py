# 38. Count and Say
# The count-and-say sequence is the sequence of integers with the first five terms as following:
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth term of the count-and-say sequence.
#
# Note: Each term of the sequence of integers will be represented as a string.
#
# Example 1:
#
# Input: 1
# Output: "1"
# Example 2:
#
# Input: 4
# Output: "1211"

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        res = "1"

        if n == 1:
            return res

        for i in range(n-1):
            res = self.getNext(res)

        return res

    def getNext(self, num):
        cur = num[0]
        count = 1
        res = ''
        for i in range(1, len(num)):
            if cur == num[i]:
                count += 1
            else:
                res += str(count)
                res += cur
                cur = num[i]
                count = 1

        res += str(count)
        res += cur
        return res