# 80. Remove Duplicates from Sorted Array II
# Difficulty: Medium
# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
#
# For example,
# Given sorted array nums = [1,1,1,2,2,3],
#
# Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3.
# It doesn't matter what you leave beyond the new length.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        idx = 1
        cout = 1
        cur = nums[0]
        idx_list = []
        while idx < len(nums):
            if cur == nums[idx]:
                cout += 1
                if cout > 2:
                    idx_list.append(idx)
            else:
                cur = nums[idx]
                cout = 1
            idx += 1

        for i in range(len(idx_list)):
            del nums[idx_list[i]-i]
        return len(nums)
if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    print Solution().removeDuplicates(nums)
    print nums