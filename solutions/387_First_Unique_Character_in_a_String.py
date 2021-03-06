# 387. First Unique Character in a String
# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
import collections

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = collections.Counter(s)
        print c

        for idx,char in enumerate(s):
            if c[char] == 1:
                return idx
        return -1
if __name__ == '__main__':
    s = "leetcode"
    print Solution().firstUniqChar(s)