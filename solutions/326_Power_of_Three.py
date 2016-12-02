# 326. Power of Three
# Difficulty: Easy
# Contributors: Admin
# Given an integer, write a function to determine if it is a power of three.
#
# Follow up:
# Could you do it without using any loop / recursion?

class Solution(object):


    def isPowerOfThree_two(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return False if n <= 0 else n == pow(3, round(math.log(n, 3)))

    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n%3 != 0 or n == 0:
            return False
        else:
            return self.isPowerOfThree(n/3)
if __name__ == '__main__':
    print Solution().isPowerOfThree(-27)
    print Solution().isPowerOfThree(36)