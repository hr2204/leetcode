# 231. Power of Two
# Difficulty: Easy
# Given an integer, write a function to determine if it is a power of two.
#


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n == 0:
            return False
        if n%2 == 0:
            return self.isPowerOfTwo(n/2)
        else:
            return False

if __name__ == "__main__":
    assert Solution().isPowerOfTwo(5) == False
    assert Solution().isPowerOfTwo(4) == True