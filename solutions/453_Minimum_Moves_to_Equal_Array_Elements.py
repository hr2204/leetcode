# 453. Minimum Moves to Equal Array Elements
# Difficulty: Easy
# Contributors:
# amehrotra2610
# Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal,
# where a move is incrementing n - 1 elements by 1.
#
# Example:
#
# Input:
# [1,2,3]
#
# Output:
# 3
#
# Explanation:
# Only three moves are needed (remember each move increments two elements):
#
# [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

class Solution(object):
    def minMoves(self, nums):
        min_num = min(nums)
        count = 0
        for num in nums:
            count += num - min_num
        return count

    def minMoves_LTE(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        while max(nums)!=min(nums):
            diff = max(nums) - min(nums)
            count += diff
            max_number_idx = nums.index(max(nums))
            for i in xrange(len(nums)):
                if i!= max_number_idx:
                    nums[i] = nums[i] + diff
        return count

if __name__ == '__main__':
    print Solution().minMoves([1,2,3])
    print Solution().minMoves([1,3,5,7])