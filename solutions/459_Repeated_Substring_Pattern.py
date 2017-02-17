# 459. Repeated Substring Pattern
# Description  Submission  Solutions  Add to List
# Total Accepted: 19141
# Total Submissions: 49357
# Difficulty: Easy
# Contributors: YuhanXu
# Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the
# substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
#
# Example 1:
# Input: "abab"
#
# Output: True
#
# Explanation: It's the substring "ab" twice.
# Example 2:
# Input: "aba"
#
# Output: False
# Example 3:
# Input: "abcabcabcabc"
#
# Output: True
#
# Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        str_len = len(str)
        for idx in range(str_len/2):
            if str_len%(idx+1) == 0 and str[:idx+1]*(str_len/(idx+1)) == str:
                return True

        return False




if __name__ == '__main__':
    input = 'abcabcabcabc'
    print Solution().repeatedSubstringPattern(input)