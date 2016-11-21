# 3. Longest Substring Without Repeating Characters
# Difficulty: Medium
# Contributors: Admin
# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring,
# "pwke" is a subsequence and not a substring.


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        next_idx = 1
        for cur_idx,cur_char in enumerate(s):
            # next_idx = cur_idx + 1
            while next_idx <len(s) and s[next_idx] not in s[cur_idx:next_idx]:
                next_idx += 1
            res = max(res,next_idx-cur_idx)
        return res

if __name__ == '__main__':
    test_case_1 = 'abcabcbb'
    test_case_2 = 'bbbbb'
    test_case_3 = 'pwwkew'
    print Solution().lengthOfLongestSubstring(test_case_1)
    print Solution().lengthOfLongestSubstring(test_case_2)
    print Solution().lengthOfLongestSubstring(test_case_3)