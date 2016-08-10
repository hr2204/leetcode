# 202. Happy Number
# Difficulty: Easy
# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
#
# Example: 19 is a happy number
#
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        numSet = set()
        return self.helper(n,numSet)
    def helper(self,n,numSet):
        if n == 1:
            return True
        elif n in numSet:
            return False
        else:
            numSet.add(n)

            if n < 10:
                n = n * n
                return self.helper(n,numSet)
            else:
                temp = 0
                while n/10 > 0:
                    temp += (n%10)*(n%10)
                    n /=10
                temp += n * n
                return self.helper(temp,numSet)
    def isHappy(self, n):
        numSet = set()
        while n != 1 and n not in numSet:
            numSet.add(n)
            sum = 0
            while n:
                digit = n % 10
                sum += digit * digit
                n /= 10
            n = sum
        return n == 1

if __name__ == "__main__":
    # assert Solution().rotate([1,2,3,4,5,6,7])
    assert Solution().isHappy(7) == True