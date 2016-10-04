# 91. Decode Ways
# Difficulty: Medium
# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.
#
# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
#
# The number of ways decoding "12" is 2.
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == "0":
            return 0

        dp = [1]
        starIdx = 1
        if s[0:2] == "10" or s[0:2] == "20":
            dp = [1,1]
            starIdx = 2

        for i in range(starIdx,len(s)):
            if s[i]!="0":
                if 1 <=int(s[i-1:i+1])<=26 and s[i-1]!="0":
                    dp.append(dp[i-1] + dp[i-2])
                else:
                    dp.append(dp[i-1])
            else:
                if int(s[i-1])>2 or int(s[i-1])<1:
                    return 0
                dp.append(dp[i-2])

        return dp[-1]



if __name__ == '__main__':
    print Solution().numDecodings("12") == 2
    print Solution().numDecodings("10") == 1
    print Solution().numDecodings("100") == 0
    print Solution().numDecodings("101") == 1
    print Solution().numDecodings("11") == 2
    print Solution().numDecodings("111") == 3





