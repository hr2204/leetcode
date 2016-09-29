# 167. Two Sum II - Input array is sorted
# Difficulty: Medium
# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
#
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
#
# You may assume that each input would have exactly one solution.
#
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2
#

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        for num in numbers:
            if num < target and self.binary_search(target-numbers)>0:

        return res


    def binary_search(self,nums,target):

        return -1

if __name__ == '__main__':
    print Solution().twoSum([2,7,11,15],9) == [1,2]
