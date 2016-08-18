# 6. ZigZag Conversion  QuestionEditorial
# Difficulty: Easy
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".


class Solution(object):

    # TLE
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) == 0:
            return ""
        if numRows == 1:
            return s
        strMatrix = []
        modNum = 2 * numRows- 2
        for i in range(modNum):
            strMatrix.append("")
        for i,char in enumerate(s):
            for j in range(modNum):
                if i% modNum == j or i% modNum == modNum - j:
                     strMatrix[j] += char

        res = ""
        for i in range(numRows):
            res += strMatrix[i]
        print strMatrix
        return res



if __name__ == '__main__':
    print Solution().convert("A",1)