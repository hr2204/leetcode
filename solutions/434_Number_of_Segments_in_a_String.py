# 434. Number of Segments in a String
# Total Accepted: 11985
# Total Submissions: 32340
# Difficulty: Easy
# Contributors: love_FDU_llp
# Count the number of segments in a string, where a segment is defined to be a
# contiguous sequence of non-space characters.
#
# Please note that the string does not contain any non-printable characters.
#
# Example:
#
# Input: "Hello, my name is John"
# Output: 5

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())