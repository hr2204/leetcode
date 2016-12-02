# 242. Valid Anagram
# Difficulty: Easy
# Given two strings s and t, write a function to determine if t is an anagram of s.
#
# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.
#
# Note:
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?

class Solution(object):

    def isAnagram_two(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)


    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sCount = self.count(s)
        tCount = self.count(t)
        return sCount == tCount
    def count(self,s):
        res = dict()
        for i in s:
            if i not in res:
                res[i] = 1
            else:
                res[i] += 1
        return res

if __name__ == "__main__":
    # assert Solution().rotate([1,2,3,4,5,6,7])
    print Solution().count("ababca")
    print Solution().isAnagram("abc","cbaa")