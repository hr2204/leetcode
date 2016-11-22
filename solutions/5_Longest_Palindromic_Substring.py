# 5. Longest Palindromic Substring
# Difficulty: Medium
# Contributors: Admin
# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example:
#
# Input: "babad"
#
# Output: "bab"
#
# Note: "aba" is also a valid answer.
# Example:
#
# Input: "cbbd"
#
# Output: "bb"


class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = [""]
        for idx in range(len(s)):
           self.get_palindrome(s,idx,idx,res)
           self.get_palindrome(s,idx,idx+1,res)
        return res[0]

    def get_palindrome(self,s,start,end,res):
        while start>-1 and end <len(s) and s[start] == s[end]:
                start -= 1
                end += 1
        if  end - start>len(res[0]):
            res[0] = s[start+1:end]

    def longestPalindrome_1(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for idx in range(len(s)):
            start = idx
            end = idx
            while start>-1 and end <len(s) and s[start] == s[end]:
                start -= 1
                end += 1

            if  end - start>len(res):
                res = s[start+1:end]
            start = idx
            end = idx+1
            while start>-1 and end <len(s) and s[start] == s[end]:
                start -= 1
                end += 1

            if  end - start>len(res):
                res = s[start+1:end]

        return res
    #
    # def isPalindrome(s,start,end):
    #     return s[start] == s[end]



if __name__ == '__main__':
    test_case_1 = "babad"
    test_case_2 = "cbbd"
    print Solution().longestPalindrome(test_case_1)
    print Solution().longestPalindrome(test_case_2)