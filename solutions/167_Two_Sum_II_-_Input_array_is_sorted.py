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
        checked = []
        for i,num in enumerate(numbers):
            if num <= target and num not in checked:
                checked.append(num)
                idx = self.binary_search(numbers[i:],target-num)
                if idx>0:
                    res.append(i+1)
                    res.append(i+idx+1)
                    break
        return res


    def binary_search(self,nums,target):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start)/2
            if nums[mid] == target:
                return mid
            if nums[mid]<target:
                start = mid
            else:
                end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

if __name__ == '__main__':
    # print Solution().binary_search([2,7,11,15],11)

    print Solution().twoSum([5,25,75],100) == [2,3]

    print Solution().twoSum([0,0,3,4],0) == [1,2]
