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
    def convert(self, s, numRows):
        if len(s) == 0:
            return ""
        if numRows == 1:
            return s
        res = ""
        modNum = 2 * numRows- 2

        # for j in range(modNum):
        # for i in range(0,len(s),modNum):
        #     res += s[i]

        for row in range(numRows):
            if row == 0 or row == numRows - 1:
                for i in range(row,len(s),modNum):
                    res += s[i]

            else:
                for i in range(row,len(s),modNum):
                    res += s[i]
                    j = i + (numRows-row - 1)*2
                    if j<len(s):
                        res += s[j]
        return res

    # TLE
    def convert_TLE(self, s, numRows):
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
    print Solution().convert("PAYPALISHIRING",3)