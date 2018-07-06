# 49. Group Anagrams
# Given an array of strings, group anagrams together.
#
# Example:
#
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:
#
# All inputs will be in lowercase.
# The order of your output does not matter.

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        temp = []
        res = {}
        for str in strs:
            temp.append((str, ''.join(sorted(str))))

        print temp
        for str in temp:
            if str[1] in res:
                res[str[1]].append(str[0])
            else:
                res[str[1]] = [str[0]]

        print res
        fres = []

        for key, value in res.items():
            fres.append(value)

        return fres