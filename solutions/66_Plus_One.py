# 66. Plus One  Q
# Difficulty: Easy
# Given a non-negative number represented as an array of digits, plus one to the number.
#
# The digits are stored such that the most significant digit is at the head of the list.


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) <= 0:
            return []
        if len(digits) == 1:
            if digits[0]!=9:
                digits[0] = digits[0] + 1
                return digits
            else:
                return [1,0]
        else:
            if digits[-1] != 9:
                digits[-1] = digits[-1] + 1
                return digits
            else:
                return self.plusOne(digits[:-1]) + [0]
if __name__ == "__main__":
    assert Solution().plusOne([1,2,9]) == [1,3,0]
