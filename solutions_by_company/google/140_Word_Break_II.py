# 140. Word Break II
# DescriptionHintsSubmissionsDiscussSolution
# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to
# construct a sentence where each word is a valid dictionary word. Return all such possible sentences.
#
# Note:
#
# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
# Example 1:
#
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
#   "cats and dog",
#   "cat sand dog"
# ]
# Example 2:
#
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
# Example 3:
#
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordDict = set(wordDict)
        self.res = []
        self.dfs(s,wordDict,"")

        return self.res

    def dfs(self,s, wordDict, stringList):
        if self.check(s, wordDict):
            if not len(s):
                    self.res.append(stringList[1:])

            for i in range(0,len(s)+1):
                if s[:i] in wordDict:
                    self.dfs(s[i:], wordDict, stringList + " " + s[:i])



    def check(self,s, wordDict):
        wordDict = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if s[j:i] in wordDict and dp[j]:
                    dp[i] = True
        return dp[len(s)]


if __name__ == '__main__':
    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    solution = Solution()
    print solution.wordBreak(s, wordDict)


    # Output:
    # [
    #   "pine apple pen apple",
    #   "pineapple pen apple",
    #   "pine applepen apple"
    # ]
