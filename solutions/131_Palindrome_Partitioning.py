# 131. Palindrome Partitioning
# Difficulty: Medium
# Contributors: Admin
# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return all possible palindrome partitioning of s.
#
# For example, given s = "aab",
# Return
#
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        Solution.res = []
        self.dfs(s,[])
        return Solution.res

    def dfs(self,s,cur_list):
        if len(s) == 0:
            Solution.res.append(cur_list)
        for i in xrange(1,len(s)+1):
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:],cur_list+[s[:i]])

    def isPalindrome(self,s):
        str_len = len(s)
        for i in xrange(len(s)):
            if s[i]!= s[len(s)-i-1]:
                return False
        return True

if __name__ == '__main__':
    s = 'aab'
    print Solution().partition(s)