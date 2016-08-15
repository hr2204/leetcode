# 28. Implement strStr()
# Difficulty: Easy
# Implement strStr().
#
# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle and not haystack:
            return 0
        haystackLen = len(haystack)
        needleLen = len(needle)
        for i in range(haystackLen - needleLen + 1):
             if haystack[i:i+needleLen] == needle:
                 return i

        return -1





if __name__ == "__main__":
    print Solution().strStr("abcd","bc")
