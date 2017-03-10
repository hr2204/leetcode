# 127. Word Ladder
# Difficulty: Medium
# Contributors: Admin
# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation
# sequence from beginWord to endWord, such that:
#
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# For example,
#
# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
#
# Note:
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# UPDATE (2017/1/20):
# The wordList parameter had been changed to a list of strings (instead of a set of strings).
# Please reload the code definition to get the latest changes.
import sys
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if self.is_next_word(beginWord,endWord) and endWord in wordList:
            return 2

        if endWord not in wordList:
            return 0

        res = sys.maxint
        checked = []
        for idx,test_word in enumerate(wordList):
            if self.is_next_word(test_word,beginWord):
                temp = self.ladderLength(test_word,endWord,wordList[:idx]+wordList[idx+1:])
                if temp != 0 and temp<res:
                    res = temp + 1
        if res == sys.maxint:
            res = 0

        return res

    def is_next_word(self,given_word,test_word):
        if len(given_word)!=len(test_word):
            return False
        diff_count = 0
        for i in xrange(len(given_word)):
            if given_word[i]!=test_word[i]:
                diff_count += 1
            if diff_count > 1:
                return False
        return True

if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print Solution().ladderLength(beginWord, endWord, wordList)
    # print Solution().is_next_word('hot','goe')