# 581. Shortest Unsorted Continuous Subarray
# Total Accepted: 4205
# Total Submissions: 13874
# Difficulty: Easy
# Contributors:
# love_Fawn
# Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order,
# then the whole array will be sorted in ascending order, too.
#
# You need to find the shortest such subarray and output its length.
#
# Example 1:
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
# Note:
# Then length of the input array is in range [1, 10,000].
# The input array may contain duplicates, so ascending order here means <=.r

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        final_list = sorted(nums)
        left, right = 0, 0
        for i in range(len(nums)):
            if nums[i]!=final_list[i]:
                left = i
                break

        for i in range(len(nums))[::-1]:
            if nums[i]!=final_list[i]:
                right = i
                break
        if left == 0 and right == 0:
            return 0

        return right - left + 1




if __name__ == '__main__':
    input = [2, 6, 4, 8, 10, 9, 15]
    print Solution().findUnsortedSubarray(input)