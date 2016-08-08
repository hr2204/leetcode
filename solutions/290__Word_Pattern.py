# 290. Word Pattern
# Difficulty: Easy
# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
#
# Examples:
# pattern = "abba", str = "dog cat cat dog" should return true.
# pattern = "abba", str = "dog cat cat fish" should return false.
# pattern = "aaaa", str = "dog cat cat dog" should return false.
# pattern = "abba", str = "dog dog dog dog" should return false.
# Notes:
# You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        wordList = str.split(" ")
        patternDict = dict()
        if len(wordList) !=len(pattern):
            return False
        dict1 = dict()
        dict2 = dict()
        for i in range(len(wordList)):
            word = wordList[i]
            patternChar = pattern[i]
            if word not in dict1:
                dict1[word] = patternChar
            else:
                if dict1[word] != patternChar:
                    return False

        for i in range(len(wordList)):
            word = wordList[i]
            patternChar = pattern[i]
            if patternChar not in dict2:
                dict2[patternChar] = word
            else:
                if dict2[patternChar] != word:
                    return False



        return True

if __name__ == "__main__":
    assert Solution().wordPattern("abba","dog cat cat dog") == True
    # Solution().wordPattern("abba","dog cat cat dog")