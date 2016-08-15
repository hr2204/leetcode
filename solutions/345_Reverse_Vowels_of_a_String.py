# 345. Reverse Vowels of a String
# Difficulty: Easy
# Write a function that takes a string as input and reverse only the vowels of a string.
#
# Example 1:
# Given s = "hello", return "holle".
#
# Example 2:
# Given s = "leetcode", return "leotcede".
#
# Note:
# The vowels does not include the letter "y".


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set(["a","e","i","o","u","A","E","I","O","U"])
        vowelsList = list()
        vowelsIdxList = list()
        s = list(s)
        for i,char in enumerate(s):
            if char in vowels:
                vowelsList.append(char)
                vowelsIdxList.append(i)
        vowelsIdxList.reverse()
        for i,idx in enumerate(vowelsIdxList):
            s[idx] = vowelsList[i]
        return "".join(s)


if __name__ == "__main__":
    assert Solution().reverseVowels("leetcode") == "leotcede"
    assert Solution().reverseVowels("hello") == "holle"