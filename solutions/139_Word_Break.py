# 139. Word Break
# Difficulty: Medium
# Contributors: Admin
# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
# determine if s can be segmented into a space-separated sequence of one or more dictionary words.
# You may assume the dictionary does not contain duplicate words.
#
# For example, given
# s = "leetcode",
# dict = ["leet", "code"].
#
# Return true because "leetcode" can be segmented as "leet code".
#
# UPDATE (2017/1/4):
# The wordDict parameter had been changed to a list of strings (instead of a set of strings).
# Please reload the code definition to get the latest changes.

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s)+1)
        dp[0] = True

        for idx in xrange(1,len(s)+1):
            for sub_idx in xrange(idx):
                if dp[sub_idx] and s[sub_idx:idx] in wordDict:
                    dp[idx] = True
        return dp[-1]

    def wordBreak_LTE(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if s in wordDict:
            return True
        if not s:
            return False

        for i in xrange(1,len(s)):
            if s[:i] in wordDict and (s[i:]in wordDict or self.wordBreak(s[i:],wordDict)):
                return True
        return False


if __name__ == '__main__':
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"

    wordDict = set(["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
    print Solution().wordBreak(s,wordDict)