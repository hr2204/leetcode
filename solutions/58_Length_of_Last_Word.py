# 58. Length of Last Word
# Difficulty: Easy
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
# return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space characters only.
#
# For example,
# Given s = "Hello World",
# return 5.


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if s == "":
            return 0
        list = s.split(" ")
        return len(list[-1])
if __name__ == '__main__':
    print Solution().lengthOfLastWord("  dar")