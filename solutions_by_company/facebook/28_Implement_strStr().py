# 28. Implement strStr()
# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Example 1:
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Clarification:
#
# What should we return when needle is an empty string? This is a great question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        len_haystack = len(haystack)
        len_needle = len(needle)

        res = -1
        for i in range(0, len_haystack - len_needle + 1):
            print i
            if haystack[i:i + len_needle] == needle:
                res = i
                break
        return res


if __name__ == '__main__':
    sol = Solution().strStr('hello','ll')
    print sol