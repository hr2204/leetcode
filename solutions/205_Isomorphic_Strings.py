# 205. Isomorphic Strings
# Difficulty: Easy
# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character but a character may map to itself.
#
# For example,
# Given "egg", "add", return true.
#
# Given "foo", "bar", return false.
#
# Given "paper", "title", return true.
#
# Note:
# You may assume both s and t have the same length.

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sDict = dict()
        tDict = dict()

        if len(s)!= len(t):
            return False
        for i in range(len(s)):
            sChar = s[i]
            tChar = t[i]
            if sChar in sDict:
                if sDict[sChar] != tChar:
                    return False
            if tChar in tDict:
                if tDict[tChar] != sChar:
                    return False
            sDict[sChar] = tChar
            tDict[tChar] = sChar

        return True


if __name__ == "__main__":
    # assert Solution().rotate([1,2,3,4,5,6,7])
    assert Solution().isIsomorphic("abbc", "ca") == False
    assert Solution().isIsomorphic("foo", "baa") == True


