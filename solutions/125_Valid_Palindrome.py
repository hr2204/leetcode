# 125. Valid Palindrome
# Difficulty: Easy
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
#
# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.
#
# For the purpose of this problem, we define empty string as valid palindrome.


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        start = 0
        end = len(s)
        while start < end:
            startChar = s[start]
            endChar = s[end - 1]
            if not startChar.isalpha() and not startChar.isdigit():
                start += 1
                continue
            if not endChar.isalpha() and not endChar.isdigit():
                end -= 1
                continue
            if startChar != endChar:
                return False
            start += 1
            end -= 1

        return True


if __name__ == "__main__":
    assert Solution().isPalindrome("A man, a plan, a canal: Panama") == True
    assert Solution().isPalindrome("0p") == False
