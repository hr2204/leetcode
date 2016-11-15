# 409. Longest Palindrome
# Difficulty: Easy
# Contributors: Admin
# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
#
# This is case sensitive, for example "Aa" is not considered a palindrome here.
#
# Note:
# Assume the length of given string will not exceed 1,010.
#
# Example:
#
# Input:
# "abccccdd"
#
# Output:
# 7
#
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
import collections
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        hasOdd = False
        letters = collections.Counter(s)
        print letters

        for num in letters.values():
            if num % 2 == 0:
                res += num
            else:
                hasOdd = True
                res += num - 1
        if hasOdd:
            res += 1
        return res

if __name__ == '__main__':
    print Solution().longestPalindrome("abccccdd")