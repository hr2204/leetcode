# 551. Student Attendance Record I
# Difficulty: Easy
# Contributors:
# fallcreek
# You are given a string representing an attendance record for a student. The record only contains the following three characters:
#
# 'A' : Absent.
# 'L' : Late.
# 'P' : Present.
# A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous
# 'L' (late).
#
# You need to return whether the student could be rewarded according to his attendance record.
#
# Example 1:
# Input: "PPALLP"
# Output: True
# Example 2:
# Input: "PPALLL"
# Output: False

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """

        count = 0

        for str in s:
            if str == 'A':
                count += 1

        idx = 0

        flag = False
        while idx < len(s):
            if s[idx] == 'L' and idx < len(s) - 2:
                if s[idx+1] == 'L' and s[idx+2] == 'L':
                    flag = True
                    break
            idx += 1
        return not (count > 1 or flag)


if __name__ == '__main__':
    input = "PPALLP"
    print Solution().checkRecord(input)