# 14. Longest Common Prefix
# Difficulty: Easy
# Write a function to find the longest common prefix string amongst an array of strings.


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        longest = ""
        if len(strs) == 0:
            return longest
        if len(strs) == 1:
            return strs[0]

        shortStr = sorted(strs, key=len)[0]
        subStr = ""
        for i in range(len(shortStr)):
            subStr = shortStr[0:i+1]
            for str in strs:
                if subStr!= str[0:i+1]:
                    return shortStr[0:i]
        return subStr
if __name__ == '__main__':
    print Solution().longestCommonPrefix(["c","c","c"])