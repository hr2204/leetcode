# 414. Third Maximum Number
# Difficulty: Easy
# Contributors: ZengRed , 1337c0d3r
# Given a non-empty array of integers, return the third maximum number in this array. If it does not exist,
# return the maximum number. The time complexity must be in O(n).
#
# Example 1:
# Input: [3, 2, 1]
#
# Output: 1
#
# Explanation: The third maximum is 1.
# Example 2:
# Input: [1, 2]
#
# Output: 2
#
# Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
# Example 3:
# Input: [2, 2, 3, 1]
#
# Output: 1
#
# Explanation: Note that the third maximum here means the third maximum distinct number.
# Both numbers with value 2 are both considered as second maximum.

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        nums = list(set(nums))
        nums.sort()
        if len(nums)<3:
            return nums[-1]
        return nums[-3]

if __name__ == '__main__':
    print Solution().thirdMax([3,2,1])
    print Solution().thirdMax([1,2,2,5,3,5])
    print Solution().thirdMax([2,2,3,1])