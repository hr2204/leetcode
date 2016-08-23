# 374. Guess Number Higher or Lower
# Difficulty: Easy
# We are playing the Guess Game. The game is as follows:
#
# I pick a number from 1 to n. You have to guess which number I picked.
#
# Every time you guess wrong, I'll tell you whether the number is higher or lower.
#
# You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):
#
# -1 : My number is lower
#  1 : My number is higher
#  0 : Congrats! You got it!
# Example:
# n = 10, I pick 6.
#
# Return 6.


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while start< end:
            mid = (start + end)/2
            if guess(mid) == 1:
                start = mid +1
            else:
                end = mid
        return start


def guess(n):
    num = 6
    if n == num:
        return 0
    elif n < num:
        return 1
    else:
        return -1

if __name__ == '__main__':
    print Solution().guessNumber(10)



