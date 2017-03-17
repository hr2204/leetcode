# 179. Largest Number
# Difficulty: Medium
# Contributors: Admin
# Given a list of non negative integers, arrange them such that they form the largest number.
#
# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
#
# Note: The result may be very large, so you need to return a string instead of an integer.

class Solution(object):
    def largestNumber(self, nums):
        """ :type nums: List[int] :rtype: str """
        def compare(a,b):
            return int(b + a) - int(a + b)
        nums = sorted([str(x) for x in nums],cmp = compare)
        ans = ''.join(nums).lstrip('0')

        return ans or '0'


if __name__ == '__main__':
    input = [3, 30, 34, 5, 9];
    print Solution().largestNumber(input)