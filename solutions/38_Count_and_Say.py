# 38. Count and Say
# Difficulty: Easy
# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
#
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.
#
# Note: The sequence of integers will be represented as a string.


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # if n == "1":
        #     return n
        temp = "1"
        idx = int(n) -1
        while idx > 0:
            temp = self.helper(temp)
            idx -= 1

        return temp

    def helper(self,n):
        res = ""
        start = 0
        count = 1
        end = start + 1
        while end <= len(n):
            if end == len(n) or n[end] != n[start]:
                res += str(count) + n[start]
                start = end
                end += 1
                count = 1
            else:
                count += 1
                end += 1
        return res


if __name__ == '__main__':
    # print Solution().countAndSay("1")
    print Solution().countAndSay("1")
    print Solution().countAndSay("2")
