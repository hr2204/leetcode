# 49. Group Anagrams   Add to List
# Difficulty: Medium
# Contributors: Admin
# Given an array of strings, group anagrams together.
#
# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Return:
#
# [
#   ["ate", "eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
#

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for w in sorted(strs):
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return d.values()

    def groupAnagrams_LTE2(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hasMap = {}
        for word in strs:
            key = "".join(sorted(word))
            if key in hasMap.keys():
                hasMap[key].append(word)
            else:
                hasMap[key] = [word]
        return hasMap.values()

    def groupAnagrams_LTE(self, strs):

        hasMap = {}
        for word in strs:
            key = [0] * 26
            for char in word:
                key[ord(char) - 97] += 1
            key = ''.join(str(x) for x in key)

            if key in hasMap.keys():
                hasMap[key].append(word)
            else:
                hasMap[key] = [word]

        # res = []
        # for key in hasMap.keys():
        #     res.append(hasMap[key])

        return hasMap.values()



if __name__ == '__main__':
    input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    solution = Solution()
    print solution.groupAnagrams(input)

