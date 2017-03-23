# 187. Repeated DNA Sequences
# Difficulty: Medium
# Contributors: Admin
# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA,
# it is sometimes useful to identify repeated sequences within the DNA.
#
# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
#
# For example,
#
# Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
#
# Return:
# ["AAAAACCCCC", "CCCCCAAAAA"].

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        hashmap = {}
        for i in xrange(len(s)-9):
            cur = s[i:i+10]
            if cur in hashmap and cur not in res:
                res.append(cur)
            else:
                hashmap[cur] = 1
        return res
if __name__ == '__main__':
    s = "AAAAAAAAAAA"
    print Solution().findRepeatedDnaSequences(s)