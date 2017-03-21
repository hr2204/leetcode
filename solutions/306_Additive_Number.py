# 306. Additive
# Difficulty: Medium
# Contributors: Admin
# Additive number is a string whose digits can form additive sequence.
#
# A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.
#
# For example:
# "112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.
#
# 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
# "199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.
# 1 + 99 = 100, 99 + 100 = 199
# Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.
#
# Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.
#
# Follow up:
# How would you handle overflow for very large input integers?

class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """

        for i in xrange(1,len(num)):
            for j in xrange(i+1,len(num)):
                # if num[i] == '0' and j-i>1:
                #     continue
                if self.helper(num[:i],num[i:j],num[j:]):
                    return True
        return False

    def helper(self,num1,num2,nums):
        if num1[0] == '0' and len(num1) > 1:
            return False
        if num2[0] == '0' and len(num2) > 1:
            return False
        num1 = int(num1)
        num2 = int(num2)
        if not nums:
            return True
        sum = str(num1+num2)
        if len(sum) > len(nums) or nums[:len(sum)]!= sum:
            return False
        return self.helper(str(num2),nums[:len(sum)],nums[len(sum):])

if __name__ == '__main__':
    # print Solution().helper(1,1,'2358')
    print Solution().isAdditiveNumber("198019823962")

    print Solution().isAdditiveNumber('123')

    print Solution().isAdditiveNumber('112358')
    print Solution().isAdditiveNumber('199100199')