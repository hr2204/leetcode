# 394. Decode String
# Difficulty: Medium
# Given an encoded string, return it's decoded string.
#
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being
# repeated exactly k times. Note that k is guaranteed to be a positive integer.
#
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
#
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those
#     repeat numbers, k. For example, there won't be input like 3a or 2[4].
#
# Examples:
#
# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        index, num = 0,0
        while index < len(s):
            char = s[index]
            if char.isdigit():
                num = num * 10 + int(char)
                index += 1
            if char == "[":
                endIdx = self.get_end_index(s[index:])
                endIdx = index + endIdx
                res += num * self.decodeString(s[index+1:endIdx])
                index = endIdx + 1
                num = 0
            if char.isalpha():
                res += char
                index += 1
        return res

    def get_end_index(self,s):
        endIdx = 0
        stack = []
        for i,char in enumerate(s):
            if char == "[":
                stack.append(char)
            if char == "]":
                stack.pop()
            if not stack:
                return i
        return endIdx
    # def dfs(self,s,res):
    #     index = 1
    #     num = s[0]
    #     temp = ""
    #     while index < len(s):
    #         if s[index].isdigit():
    #             temp += self.dfs(s,res)
    #         else:
    #             temp += s[index]
    #             index += 1
    #
    #     return num * temp

if __name__ == '__main__':
    print Solution().decodeString("3[a2[c]]")
    # print Solution().decodeString("aa3[b]cc")
