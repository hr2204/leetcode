# 400. Nth Digit   QuestionEditorial Solution
# Difficulty: Easy
# Contributors: Admin
# Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...
#
# Note:
# n is positive and will fit within the range of a 32-bit signed integer (n < 231).
#
# Example 1:
#
# Input:
# 3
#
# Output:
# 3
# Example 2:
#
# Input:
# 11
#
# Output:
# 0
#
# Explanation:
# The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        num_of_digit = 1
        total_num = 9
        while n > total_num:
            num_of_digit += 1
            total_num += num_of_digit * 9 * pow(10,num_of_digit-1)

        total_num -= num_of_digit * 9 * pow(10,num_of_digit-1)

        digit = (n - total_num)%num_of_digit
        if digit:
            more_than = (n - total_num)/(num_of_digit)+ 1
        else:
            more_than = (n - total_num)/(num_of_digit)
            digit = num_of_digit
        number = more_than + pow(10,num_of_digit-1) - 1
        print number, digit,total_num

        return (number/pow(10,num_of_digit-digit))%10

        # number =  more_than + total_num/10
        # print number,num_of_digit
        # digit_num = pow(10,(n - total_num/10)%(num_of_digit))
        # # print number, digit_num,num_of_digit
        # return (number/digit_num)%10


if __name__ == '__main__':
    print Solution().findNthDigit(100)
