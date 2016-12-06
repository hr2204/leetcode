# 390. Elimination Game   Add to List QuestionEditorial Solution  My Submissions
# Total Accepted: 5262
# Total Submissions: 14375
# Difficulty: Medium
# Contributors: Admin
# There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other
# number afterward until you reach the end of the list.
#
# Repeat the previous step again, but this time from right to left, remove the right most number and every other number
# from the remaining numbers.
#
# We keep repeating the steps again, alternating left to right and right to left, until a single number remains.
#
# Find the last number that remains starting with a list of length n.
#
# Example:
#
# Input:
# n = 9,
# 1 2 3 4 5 6 7 8 9
# 2 4 6 8
# 2 6
# 6
#
# Output:
# 6

class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.res = 0
        self.rec(range(1,n+1),"left",self.res)
        return self.res

    def rec(self,list,dir,res):
        if len(list) == 1:
            self.res = list[0]
            return
        if dir == "left":
            self.rec(list[1::2],"right",res)
        if dir == "right":
            self.rec(list[::-1][1::2][::-1],"left",res)
if __name__ == '__main__':
    print Solution().lastRemaining(9)